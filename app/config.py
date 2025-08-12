"""Configurações da aplicação."""
import os
from typing import Optional

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Configurações da aplicação carregadas de variáveis de ambiente."""
    
    # Evolution API
    evolution_base_url: str = Field(..., env="EVOLUTION_BASE_URL")
    evolution_api_key: str = Field(..., env="EVOLUTION_API_KEY")
    evolution_instance_name: str = Field(..., env="EVOLUTION_INSTANCE_NAME")
    
    # OpenAI
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4o-mini", env="OPENAI_MODEL")
    bot_system_prompt: str = Field(
        default="Você é um assistente educado e direto.",
        env="BOT_SYSTEM_PROMPT"
    )
    
    # Webhook
    webhook_secret: Optional[str] = Field(None, env="WEBHOOK_SECRET")
    
    # Servidor
    port: int = Field(default=8080, env="PORT")
    
    # Segurança
    internal_api_token: str = Field(..., env="INTERNAL_API_TOKEN")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Instância global das configurações
settings = Settings()
