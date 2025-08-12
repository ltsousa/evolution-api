"""Configuração do pytest."""
import pytest
import asyncio
from typing import AsyncGenerator
from fastapi.testclient import TestClient
import respx

from app.main import app
from app.config import settings


@pytest.fixture
def event_loop():
    """Cria loop de eventos para testes assíncronos."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def client() -> TestClient:
    """Cliente de teste FastAPI."""
    return TestClient(app)


@pytest.fixture
def mock_evolution_api():
    """Mock da Evolution API."""
    with respx.mock(base_url=settings.evolution_base_url) as respx_mock:
        yield respx_mock


@pytest.fixture
def mock_openai_api():
    """Mock da OpenAI API."""
    with respx.mock(base_url="https://api.openai.com") as respx_mock:
        yield respx_mock


@pytest.fixture
def sample_webhook_payload():
    """Payload de exemplo para webhook."""
    return {
        "event": "messages.upsert",
        "instance": "whatsapp-teste",
        "data": {
            "data": {
                "key": {
                    "id": "test_message_id",
                    "remoteJid": "5511999999999@s.whatsapp.net",
                    "fromMe": False
                },
                "message": {
                    "conversation": "Olá, como você está?",
                },
                "messageTimestamp": "1703123456",
                "type": "text"
            }
        }
    }


@pytest.fixture
def sample_outgoing_message():
    """Mensagem de exemplo para envio."""
    return {
        "to": "5511999999999",
        "text": "Olá! Tudo bem?",
        "reply_to": None
    }


@pytest.fixture
def internal_auth_headers():
    """Headers de autorização para endpoints internos."""
    return {"Authorization": f"Bearer {settings.internal_api_token}"}
