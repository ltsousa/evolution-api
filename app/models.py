"""Modelos de dados da aplicação."""
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class IncomingMessage(BaseModel):
    """Mensagem recebida via webhook."""
    id: str
    from_number: str = Field(..., alias="from")
    to_number: str = Field(..., alias="to")
    text: Optional[str] = None
    timestamp: datetime
    type: str
    raw_data: Dict[str, Any] = Field(..., alias="raw_data")
    
    class Config:
        populate_by_name = True


class OutgoingMessage(BaseModel):
    """Mensagem a ser enviada."""
    to: str = Field(..., description="Número de telefone de destino")
    text: str = Field(..., description="Texto da mensagem")
    reply_to: Optional[str] = Field(None, description="ID da mensagem para responder")


class MessageResponse(BaseModel):
    """Resposta de envio de mensagem."""
    success: bool
    message_id: Optional[str] = None
    error: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class InstanceStatus(BaseModel):
    """Status da instância WhatsApp."""
    name: str
    status: str
    connected: bool
    qr_code: Optional[str] = None
    error: Optional[str] = None


class WebhookPayload(BaseModel):
    """Payload do webhook da Evolution API."""
    event: str
    instance: str
    data: Dict[str, Any]


class HealthResponse(BaseModel):
    """Resposta do healthcheck."""
    status: str = "healthy"
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    version: str = "1.0.0"
