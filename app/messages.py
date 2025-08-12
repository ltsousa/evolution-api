"""Roteador para envio programático de mensagens."""
import time
from datetime import datetime
from typing import Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Header
import structlog

from .models import OutgoingMessage, MessageResponse
from .evolution_client import EvolutionClient
from .queue import message_queue
from .config import settings

logger = structlog.get_logger()
router = APIRouter(prefix="/messages", tags=["messages"])

# Cliente Evolution
evolution_client = EvolutionClient()


async def verify_internal_token(authorization: str = Header(...)) -> bool:
    """Verifica token de autorização para endpoints internos."""
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")
    
    token = authorization.replace("Bearer ", "")
    if token != settings.internal_api_token:
        raise HTTPException(status_code=403, detail="Acesso negado")
    
    return True


@router.post("/send", response_model=MessageResponse)
async def send_message(
    message: OutgoingMessage,
    authorized: bool = Depends(verify_internal_token)
) -> MessageResponse:
    """Envia mensagem programaticamente."""
    start_time = time.time()
    
    try:
        logger.info(
            "Enviando mensagem programática",
            to=message.to,
            text_length=len(message.text)
        )
        
        # Enviar via Evolution API
        response = await evolution_client.send_text(
            to=message.to,
            text=message.text,
            reply_to=message.reply_to
        )
        
        # Marcar chat como não lido para o usuário
        try:
            message_id = f"prog_{int(time.time())}"
            await evolution_client.mark_chat_unread(
                number=message.to,
                last_message=message.text,
                message_id=message_id
            )
            logger.info(
                "Chat marcado como não lido",
                number=message.to
            )
        except Exception as e:
            logger.warning(
                "Erro ao marcar chat como não lido",
                number=message.to,
                error=str(e)
            )
        
        # Adicionar à fila para processamento assíncrono (opcional)
        await message_queue.enqueue({
            "id": f"prog_{int(time.time())}",
            "to": message.to,
            "text": message.text,
            "type": "programmatic"
        })
        
        latency_ms = int((time.time() - start_time) * 1000)
        logger.info(
            "Mensagem enviada com sucesso",
            to=message.to,
            message_id=response.get("key", {}).get("id"),
            latency_ms=latency_ms
        )
        
        return MessageResponse(
            success=True,
            message_id=response.get("key", {}).get("id"),
            timestamp=datetime.utcnow()
        )
        
    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)
        logger.error(
            "Erro ao enviar mensagem",
            to=message.to,
            error=str(e),
            latency_ms=latency_ms
        )
        
        return MessageResponse(
            success=False,
            error=str(e),
            timestamp=datetime.utcnow()
        )


@router.get("/stats")
async def get_message_stats(
    authorized: bool = Depends(verify_internal_token)
) -> Dict[str, Any]:
    """Retorna estatísticas de mensagens."""
    try:
        queue_stats = message_queue.get_stats()
        idempotency_stats = idempotency_manager.get_stats()
        
        return {
            "queue": queue_stats,
            "idempotency": idempotency_stats,
            "timestamp": datetime.utcnow().isoformat()
        }
        
    except Exception as e:
        logger.error("Erro ao obter estatísticas", error=str(e))
        raise HTTPException(status_code=500, detail="Erro interno")
