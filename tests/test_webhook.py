"""Testes para webhook."""
import pytest
from fastapi.testclient import TestClient
import respx

from app.config import settings


def test_webhook_handler_success(
    client: TestClient,
    mock_evolution_api,
    mock_openai_api,
    sample_webhook_payload
):
    """Testa processamento bem-sucedido de webhook."""
    # Mock OpenAI
    mock_openai_api.post("/v1/chat/completions").mock(
        return_value={
            "choices": [{"message": {"content": "Olá! Tudo bem, obrigado por perguntar!"}}]
        }
    )
    
    # Mock Evolution API
    mock_evolution_api.post("/message/sendText").mock(
        return_value={"key": {"id": "sent_message_id"}}
    )
    
    response = client.post("/webhook/", json=sample_webhook_payload)
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_webhook_handler_duplicate_message(
    client: TestClient,
    sample_webhook_payload
):
    """Testa tratamento de mensagem duplicada."""
    # Enviar primeira vez
    response1 = client.post("/webhook/", json=sample_webhook_payload)
    assert response1.status_code == 200
    
    # Enviar segunda vez (deve ser tratada como duplicada)
    response2 = client.post("/webhook/", json=sample_webhook_payload)
    assert response2.status_code == 200


def test_webhook_handler_unsupported_event(
    client: TestClient
):
    """Testa evento não suportado."""
    payload = {
        "event": "unsupported_event",
        "instance": "whatsapp-teste",
        "data": {}
    }
    
    response = client.post("/webhook/", json=payload)
    assert response.status_code == 200


def test_webhook_handler_non_text_message(
    client: TestClient
):
    """Testa mensagem que não é de texto."""
    payload = {
        "event": "messages.upsert",
        "instance": "whatsapp-teste",
        "data": {
            "data": {
                "key": {
                    "id": "test_message_id",
                    "remoteJid": "5511999999999@s.whatsapp.net",
                    "fromMe": False
                },
                "message": {},
                "messageTimestamp": "1703123456",
                "type": "image"  # Não é texto
            }
        }
    }
    
    response = client.post("/webhook/", json=payload)
    assert response.status_code == 200


def test_webhook_handler_malformed_payload(
    client: TestClient
):
    """Testa payload malformado."""
    payload = {
        "event": "messages.upsert",
        "instance": "whatsapp-teste",
        # Dados faltando
    }
    
    response = client.post("/webhook/", json=payload)
    assert response.status_code == 422  # Erro de validação


def test_webhook_handler_openai_error(
    client: TestClient,
    mock_openai_api,
    sample_webhook_payload
):
    """Testa erro na OpenAI."""
    # Mock OpenAI com erro
    mock_openai_api.post("/v1/chat/completions").mock(
        return_value=500,  # Erro interno
        status_code=500
    )
    
    response = client.post("/webhook/", json=sample_webhook_payload)
    assert response.status_code == 500


def test_webhook_handler_evolution_error(
    client: TestClient,
    mock_evolution_api,
    mock_openai_api,
    sample_webhook_payload
):
    """Testa erro na Evolution API."""
    # Mock OpenAI
    mock_openai_api.post("/v1/chat/completions").mock(
        return_value={
            "choices": [{"message": {"content": "Resposta de teste"}}]
        }
    )
    
    # Mock Evolution API com erro
    mock_evolution_api.post("/message/sendText").mock(
        return_value=500,  # Erro interno
        status_code=500
    )
    
    response = client.post("/webhook/", json=sample_webhook_payload)
    assert response.status_code == 500
