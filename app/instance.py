"""Roteador para gerenciamento de instâncias WhatsApp."""
import time
from typing import Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Header, Response
from fastapi.responses import HTMLResponse
import structlog

from .models import InstanceStatus
from .evolution_client import EvolutionClient
from .config import settings

logger = structlog.get_logger()
router = APIRouter(prefix="/instance", tags=["instance"])

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


@router.post("/ensure", response_model=InstanceStatus)
async def ensure_instance(
    authorized: bool = Depends(verify_internal_token)
) -> InstanceStatus:
    """Garante que a instância existe e está rodando."""
    start_time = time.time()
    instance_name = settings.evolution_instance_name
    
    try:
        logger.info("Verificando instância", instance_name=instance_name)
        
        # Verificar se a instância existe
        instance = await evolution_client.get_instance(instance_name)
        
        if not instance:
            logger.info("Instância não existe, criando...", instance_name=instance_name)
            instance = await evolution_client.create_instance(instance_name)
        
        # Verificar status da instância
        instance_status = instance.get("status", "unknown")
        
        if instance_status not in ["open", "connected"]:
            logger.info("Instância não está conectada, iniciando...", instance_name=instance_name)
            await evolution_client.start_instance(instance_name)
            instance_status = "starting"
        
        latency_ms = int((time.time() - start_time) * 1000)
        logger.info(
            "Instância verificada",
            instance_name=instance_name,
            status=instance_status,
            latency_ms=latency_ms
        )
        
        return InstanceStatus(
            name=instance_name,
            status=instance_status,
            connected=instance_status in ["open", "connected"],
            error=None
        )
        
    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)
        logger.error(
            "Erro ao verificar instância",
            instance_name=instance_name,
            error=str(e),
            latency_ms=latency_ms
        )
        
        return InstanceStatus(
            name=instance_name,
            status="error",
            connected=False,
            error=str(e)
        )


@router.get("/qr", response_class=HTMLResponse)
async def get_qr_code(
    authorized: bool = Depends(verify_internal_token)
) -> HTMLResponse:
    """Retorna página HTML com QR code da instância."""
    start_time = time.time()
    instance_name = settings.evolution_instance_name
    
    try:
        logger.info("Obtendo QR code", instance_name=instance_name)
        
        # Obter QR code
        qr_code = await evolution_client.get_qr(instance_name)
        
        if not qr_code:
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>QR Code - {instance_name}</title>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: Arial, sans-serif; text-align: center; padding: 20px; }}
                    .error {{ color: red; }}
                </style>
            </head>
            <body>
                <h1>QR Code não disponível</h1>
                <p class="error">Instância: {instance_name}</p>
                <p>Verifique se a instância está rodando e tente novamente.</p>
            </body>
            </html>
            """
            return HTMLResponse(content=html_content, status_code=404)
        
        # Gerar HTML com QR code
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>QR Code - {instance_name}</title>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; padding: 20px; }}
                .qr-container {{ margin: 20px auto; }}
                .instructions {{ margin: 20px; color: #666; }}
            </style>
        </head>
        <body>
            <h1>Conecte seu WhatsApp</h1>
            <p>Instância: {instance_name}</p>
            <div class="qr-container">
                <img src="data:image/png;base64,{qr_code}" alt="QR Code WhatsApp" />
            </div>
            <div class="instructions">
                <p>1. Abra o WhatsApp no seu celular</p>
                <p>2. Toque em Menu > WhatsApp Web</p>
                <p>3. Aponte a câmera para o QR code acima</p>
            </div>
            <script>
                // Atualizar QR code a cada 30 segundos
                setTimeout(() => {{ location.reload(); }}, 30000);
            </script>
        </body>
        </html>
        """
        
        latency_ms = int((time.time() - start_time) * 1000)
        logger.info(
            "QR code gerado com sucesso",
            instance_name=instance_name,
            latency_ms=latency_ms
        )
        
        return HTMLResponse(content=html_content)
        
    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)
        logger.error(
            "Erro ao obter QR code",
            instance_name=instance_name,
            error=str(e),
            latency_ms=latency_ms
        )
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Erro - QR Code</title>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; padding: 20px; }}
                .error {{ color: red; }}
            </style>
        </head>
        <body>
            <h1>Erro ao obter QR Code</h1>
            <p class="error">{str(e)}</p>
        </body>
        </html>
        """
        
        return HTMLResponse(content=html_content, status_code=500)


@router.get("/status", response_model=InstanceStatus)
async def get_instance_status(
    authorized: bool = Depends(verify_internal_token)
) -> InstanceStatus:
    """Retorna status atual da instância."""
    try:
        instance_name = settings.evolution_instance_name
        instance = await evolution_client.get_instance(instance_name)
        
        if not instance:
            return InstanceStatus(
                name=instance_name,
                status="not_found",
                connected=False,
                error="Instância não encontrada"
            )
        
        status = instance.get("status", "unknown")
        connected = status in ["open", "connected"]
        
        return InstanceStatus(
            name=instance_name,
            status=status,
            connected=connected,
            error=None
        )
        
    except Exception as e:
        logger.error("Erro ao obter status da instância", error=str(e))
        return InstanceStatus(
            name=settings.evolution_instance_name,
            status="error",
            connected=False,
            error=str(e)
        )
