"""Sistema de idempotência para mensagens."""
import asyncio
import time
from typing import Dict, Optional
from cachetools import TTLCache
import structlog

logger = structlog.get_logger()


class IdempotencyManager:
    """Gerencia idempotência de mensagens."""
    
    def __init__(self, ttl_hours: int = 24) -> None:
        self.cache: TTLCache[str, float] = TTLCache(
            maxsize=10000, 
            ttl=ttl_hours * 3600
        )
        self._lock = asyncio.Lock()
    
    async def is_duplicate(self, message_id: str) -> bool:
        """Verifica se a mensagem é duplicada."""
        async with self._lock:
            current_time = time.time()
            
            if message_id in self.cache:
                logger.info("Mensagem duplicada detectada", message_id=message_id)
                return True
            
            self.cache[message_id] = current_time
            return False
    
    async def mark_processed(self, message_id: str) -> None:
        """Marca mensagem como processada."""
        async with self._lock:
            current_time = time.time()
            self.cache[message_id] = current_time
            logger.debug("Mensagem marcada como processada", message_id=message_id)
    
    def get_stats(self) -> Dict[str, int]:
        """Retorna estatísticas do cache."""
        return {
            "total_messages": len(self.cache),
            "cache_size": self.cache.maxsize,
        }


# Instância global
idempotency_manager = IdempotencyManager()
