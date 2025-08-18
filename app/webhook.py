"""Webhook para receber mensagens da Evolution API."""
import time
from datetime import datetime
from typing import Dict, Any
from fastapi import APIRouter, Request, HTTPException, Depends
import structlog
import asyncio

from .models import WebhookPayload, IncomingMessage
from .evolution_client import EvolutionClient
from .openai_client import OpenAIClient
from .idempotency import idempotency_manager
from .config import settings

logger = structlog.get_logger()
router = APIRouter(prefix="/webhook", tags=["webhook"])

# Clientes
evolution_client = EvolutionClient()
openai_client = OpenAIClient()


async def verify_webhook_signature(request: Request) -> bool:
    """Verifica assinatura do webhook (opcional)."""
    if not settings.webhook_secret:
        return True
    
    # Implementar verificação de assinatura se necessário
    return True


@router.post("/")
async def webhook_handler(
    payload: WebhookPayload,
    request: Request,
    verified: bool = Depends(verify_webhook_signature)
) -> Dict[str, str]:
    """Processa webhook da Evolution API."""
    start_time = time.time()
    request_id = request.headers.get("X-Request-ID", "unknown")
    
    logger.info(
        "Webhook recebido",
        event_type=payload.event,
        instance=payload.instance,
        request_id=request_id
    )
    
    try:
        # Processar apenas mensagens de texto
        if payload.event == "messages.upsert":
            await _process_message(payload.data, request_id)
        elif payload.event == "connection.update":
            logger.info("Status da conexão atualizado", status=payload.data.get("state"))
        else:
            logger.debug("Evento não suportado", event_type=payload.event)
        
        latency_ms = int((time.time() - start_time) * 1000)
        logger.info(
            "Webhook processado com sucesso",
            event_type=payload.event,
            request_id=request_id,
            latency_ms=latency_ms
        )
        
        return {"status": "ok"}
        
    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)
        logger.error(
            "Erro ao processar webhook",
            event_type=payload.event,
            request_id=request_id,
            error=str(e),
            latency_ms=latency_ms
        )
        raise HTTPException(status_code=500, detail="Erro interno")


async def _process_message(data: Dict[str, Any], request_id: str) -> None:
    """Processa mensagem recebida."""
    try:
        print(f"🔍 PROCESSANDO MENSAGEM: {data}")  # Log simples para debug
        logger.info("Processando mensagem recebida", data=data, request_id=request_id)
        
        # Extrair dados da mensagem (estrutura do Evolution API)
        message_data = data
        
        # Verificar se é mensagem de texto (Evolution API usa messageType)
        message_type = message_data.get("messageType", "")
        if message_type not in ["conversation", "extendedTextMessage"]:
            print(f"❌ MENSAGEM NÃO É DE TEXTO: {message_type}")
            logger.debug("Mensagem não é de texto", messageType=message_type)
            return
        
        print(f"✅ MENSAGEM É DE TEXTO: {message_type}")
        
        # Normalizar para DTO interno
        message_content = message_data.get("message", {})
        
        # Extrair texto baseado no tipo de mensagem
        text = ""
        if message_type == "conversation":
            text = message_content.get("conversation", "")
        elif message_type == "extendedTextMessage":
            text = message_content.get("extendedTextMessage", {}).get("text", "")
        
        message = IncomingMessage(
            id=message_data.get("key", {}).get("id", ""),
            from_number=message_data.get("key", {}).get("remoteJid", ""),
            to_number="bot",  # Sempre será o bot quando recebemos mensagem
            text=text,
            timestamp=datetime.fromtimestamp(
                int(message_data.get("messageTimestamp", 0))
            ),
            type=message_type,
            raw_data=data
        )
        
        print(f"✅ MENSAGEM NORMALIZADA: {message.text}")
        
        # Verificar idempotência
        if await idempotency_manager.is_duplicate(message.id):
            print(f"❌ MENSAGEM DUPLICADA: {message.id}")
            logger.info("Mensagem duplicada ignorada", message_id=message.id)
            return
        
        print(f"✅ MENSAGEM NÃO É DUPLICADA: {message.id}")
        
        # Gerar resposta com OpenAI
        print(f"🤖 GERANDO RESPOSTA COM IA...")
        reply_text = await openai_client.generate_reply(
            message.text or "",
            context={"conversation": f"Usuário: {message.text}"}
        )
        
        print(f"✅ RESPOSTA GERADA: {reply_text[:100]}...")
        
        # Enviar resposta via Evolution
        print(f"📤 ENVIANDO RESPOSTA VIA EVOLUTION...")
        await evolution_client.send_text(
            to=message.from_number,
            text=reply_text,
            reply_to=message.id
        )
        
        print(f"✅ RESPOSTA ENVIADA")
        
        # Marcar chat como não lido para o usuário
        print(f"🔴 MARCANDO CHAT COMO NÃO LIDO...")
        try:
            # Estratégia: Aguardar um pouco para contornar o comportamento do WhatsApp
            print(f"⏳ Aguardando 5 segundos antes de marcar como não lido...")
            await asyncio.sleep(5)
            
            # Corrigir: remover @s.whatsapp.net e usar message_id único
            clean_number = message.from_number.replace("@s.whatsapp.net", "")
            unique_message_id = f"webhook_{int(time.time())}"
            
            await evolution_client.mark_chat_unread(
                number=clean_number,
                last_message=reply_text,
                message_id=unique_message_id
            )
            print(f"✅ CHAT MARCADO COMO NÃO LIDO - Número: {clean_number}, ID: {unique_message_id}")
            logger.info(
                "Chat marcado como não lido",
                number=clean_number,
                message_id=unique_message_id,
                request_id=request_id
            )
        except Exception as e:
            print(f"❌ ERRO AO MARCAR COMO NÃO LIDO: {e}")
            logger.warning(
                "Erro ao marcar chat como não lido",
                number=message.from_number,
                error=str(e),
                request_id=request_id
            )
        
        # Marcar como processada
        await idempotency_manager.mark_processed(message.id)
        
        logger.info(
            "Mensagem processada com sucesso",
            message_id=message.id,
            from_number=message.from_number,
            reply_length=len(reply_text),
            request_id=request_id
        )
        
    except Exception as e:
        logger.error("Erro ao processar mensagem", error=str(e), request_id=request_id)
        raise
