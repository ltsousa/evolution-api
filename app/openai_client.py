"""Cliente para OpenAI API."""
from typing import Dict, Optional
from openai import AsyncOpenAI
import structlog
from tenacity import retry, stop_after_attempt, wait_exponential

from .config import settings

logger = structlog.get_logger()

# Configurar OpenAI
openai_client = AsyncOpenAI(api_key=settings.openai_api_key)


class OpenAIClient:
    """Cliente para OpenAI API."""
    
    def __init__(self) -> None:
        self.model = settings.openai_model
        self.system_prompt = settings.bot_system_prompt
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def generate_reply(
        self, 
        user_text: str, 
        context: Optional[Dict[str, str]] = None
    ) -> str:
        """Gera resposta usando OpenAI."""
        try:
            messages = [{"role": "system", "content": self.system_prompt}]
            
            if context:
                context_text = f"Contexto: {context.get('conversation', '')}"
                messages.append({"role": "system", "content": context_text})
            
            messages.append({"role": "user", "content": user_text})
            
            response = await openai_client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.7,
            )
            
            reply = response.choices[0].message.content.strip()
            logger.info("Resposta OpenAI gerada", user_text=user_text[:100], reply=reply[:100])
            
            return reply
            
        except Exception as e:
            logger.error("Erro ao gerar resposta OpenAI", error=str(e))
            return "Desculpe, não consegui processar sua mensagem no momento. Tente novamente mais tarde."