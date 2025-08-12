"""Sistema de fila para envio de mensagens."""
import asyncio
from typing import Any, Callable, Dict, Optional
import structlog
from tenacity import retry, stop_after_attempt, wait_exponential

logger = structlog.get_logger()


class MessageQueue:
    """Fila assíncrona para envio de mensagens."""
    
    def __init__(self) -> None:
        self.queue: asyncio.Queue = asyncio.Queue()
        self.consumer_task: Optional[asyncio.Task] = None
        self.is_running = False
    
    async def start(self) -> None:
        """Inicia o consumidor da fila."""
        if not self.is_running:
            self.is_running = True
            self.consumer_task = asyncio.create_task(self._consumer())
            logger.info("Fila de mensagens iniciada")
    
    async def stop(self) -> None:
        """Para o consumidor da fila."""
        if self.is_running:
            self.is_running = False
            if self.consumer_task:
                self.consumer_task.cancel()
                try:
                    await self.consumer_task
                except asyncio.CancelledError:
                    pass
            logger.info("Fila de mensagens parada")
    
    async def enqueue(self, message: Dict[str, Any]) -> None:
        """Adiciona mensagem à fila."""
        await self.queue.put(message)
        logger.debug("Mensagem adicionada à fila", message_id=message.get("id"))
    
    async def _consumer(self) -> None:
        """Consumidor da fila."""
        while self.is_running:
            try:
                message = await asyncio.wait_for(self.queue.get(), timeout=1.0)
                await self._process_message(message)
                self.queue.task_done()
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                logger.error("Erro no consumidor da fila", error=str(e))
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def _process_message(self, message: Dict[str, Any]) -> None:
        """Processa mensagem da fila."""
        try:
            # Aqui você implementaria a lógica de envio
            # Por enquanto, apenas logamos
            logger.info("Processando mensagem da fila", message=message)
            
            # Simular processamento
            await asyncio.sleep(0.1)
            
        except Exception as e:
            logger.error("Erro ao processar mensagem", message=message, error=str(e))
            raise
    
    def get_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas da fila."""
        return {
            "queue_size": self.queue.qsize(),
            "is_running": self.is_running,
            "consumer_active": self.consumer_task is not None and not self.consumer_task.done()
        }


# Instância global
message_queue = MessageQueue()
