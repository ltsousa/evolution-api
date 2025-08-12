"""Roteador para webhooks da Evolution API."""
import time
from datetime import datetime
from typing import Any, Dict
from fastapi import APIRouter, Request, HTTPException, Depends
import structlog

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
        # Extrair dados da mensagem
        message_data = data.get("data", {})
        
        # Verificar se é mensagem de texto
        if message_data.get("type") != "text":
            logger.debug("Mensagem não é de texto", type=message_data.get("type"))
            return
        
        # Normalizar para DTO interno
        message = IncomingMessage(
            id=message_data.get("key", {}).get("id", ""),
            from_number=message_data.get("key", {}).get("remoteJid", ""),
            to_number="bot",  # Sempre será o bot quando recebemos mensagem
            text=message_data.get("message", {}).get("conversation", ""),
            timestamp=datetime.fromtimestamp(
                int(message_data.get("messageTimestamp", 0))
            ),
            type=message_data.get("type", ""),
            raw_data=data
        )
        
        # Verificar idempotência
        if await idempotency_manager.is_duplicate(message.id):
            logger.info("Mensagem duplicada ignorada", message_id=message.id)
            return
        
        # Gerar resposta com OpenAI
        reply_text = await openai_client.generate_reply(
            message.text or "",
            context={"conversation": f"Usuário: {message.text}"}
        )
        
        # Enviar resposta via Evolution
        await evolution_client.send_text(
            to=message.from_number,
            text=reply_text,
            reply_to=message.id
        )
        
        # Marcar chat como não lido para o usuário
        try:
            await evolution_client.mark_chat_unread(
                number=message.from_number,
                last_message=reply_text,
                message_id=message.id
            )
            logger.info(
                "Chat marcado como não lido",
                number=message.from_number,
                request_id=request_id
            )
        except Exception as e:
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
