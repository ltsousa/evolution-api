"""Cliente para Evolution API v2."""
import asyncio
from typing import Dict, Optional, Any
import httpx
import structlog
from tenacity import retry, stop_after_attempt, wait_exponential
import time

from .config import settings

logger = structlog.get_logger()


class EvolutionClient:
    """Cliente para Evolution API v2."""
    
    def __init__(self) -> None:
        self.base_url = settings.evolution_base_url.rstrip("/")
        self.api_key = settings.evolution_api_key
        self.headers = {
            "apikey": self.api_key,
            "Content-Type": "application/json",
        }
    
    async def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Faz requisição para Evolution API."""
        url = f"{self.base_url}{endpoint}"
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method, url, headers=self.headers, json=data
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 429:
                    logger.warning("Rate limit atingido, aguardando...")
                    await asyncio.sleep(2)
                    raise
                logger.error("Erro HTTP", status_code=e.response.status_code, error=str(e))
                raise
            except Exception as e:
                logger.error("Erro na requisição", error=str(e))
                raise
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def get_instance(self, name: str) -> Optional[Dict[str, Any]]:
        """Obtém informações da instância."""
        try:
            # Primeiro busca todas as instâncias
            response = await self._make_request("GET", "/instance/fetchInstances")
            instances = response if isinstance(response, list) else []
            
            # Procura pela instância específica
            for instance in instances:
                if instance.get("name") == name:
                    return instance
            return None
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def create_instance(self, name: str) -> Dict[str, Any]:
        """Cria nova instância."""
        data = {"instanceName": name}
        return await self._make_request("POST", "/instance/create", data)
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def start_instance(self, name: str) -> Dict[str, Any]:
        """Inicia instância existente."""
        data = {"instanceName": name}
        return await self._make_request("POST", "/instance/start", data)
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def get_qr(self, name: str) -> Optional[str]:
        """Obtém QR code da instância."""
        try:
            response = await self._make_request("GET", f"/instance/connect/{name}")
            return response.get("qrcode")
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def send_text(self, to: str, text: str, reply_to: Optional[str] = None) -> Dict[str, Any]:
        """Envia mensagem de texto."""
        data = {
            "number": to,
            "text": text,
        }
        if reply_to:
            data["reply_to"] = reply_to
            
        # Usar o endpoint correto da Evolution API v2
        return await self._make_request("POST", f"/message/sendText/{settings.evolution_instance_name}", data)
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def send_media(
        self, 
        to: str, 
        media_url: str, 
        caption: Optional[str] = None
    ) -> Dict[str, Any]:
        """Envia mídia."""
        data = {
            "number": to,
            "media": media_url,
        }
        if caption:
            data["caption"] = caption
            
        # Usar o endpoint correto da Evolution API v2
        return await self._make_request("POST", f"/message/sendMedia/{settings.evolution_instance_name}", data)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def mark_chat_unread(self, number: str, last_message: str, message_id: str = None) -> Dict[str, Any]:
        """Marca chat como não lido."""
        # Formato correto da Evolution API v2
        data = {
            "lastMessage": {
                "key": {
                    "remoteJid": f"{number}@s.whatsapp.net",
                    "fromMe": False,
                    "id": message_id or f"bot_{int(time.time())}"
                }
            },
            "chat": f"{number}@s.whatsapp.net"
        }
        
        return await self._make_request("POST", f"/chat/markChatUnread/{settings.evolution_instance_name}", data)
