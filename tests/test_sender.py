"""Testes para envio de mensagens."""
import pytest
from fastapi.testclient import TestClient
import respx

from app.config import settings


def test_send_message_success(
    client: TestClient,
    mock_evolution_api,
    sample_outgoing_message,
    internal_auth_headers
):
    """Testa envio bem-sucedido de mensagem."""
    # Mock Evolution API
    mock_evolution_api.post("/message/sendText").mock(
        return_value={"key": {"id": "sent_message_id"}}
    )
    
    response = client.post(
        "/messages/send",
        json=sample_outgoing_message,
        headers=internal_auth_headers
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["message_id"] == "sent_message_id"
    assert "error" not in data


def test_send_message_unauthorized(
    client: TestClient,
    sample_outgoing_message
):
    """Testa envio sem autorização."""
    response = client.post("/messages/send", json=sample_outgoing_message)
    assert response.status_code == 422  # Falta header Authorization


def test_send_message_invalid_token(
    client: TestClient,
    sample_outgoing_message
):
    """Testa envio com token inválido."""
    headers = {"Authorization": "Bearer invalid_token"}
    
    response = client.post(
        "/messages/send",
        json=sample_outgoing_message,
        headers=headers
    )
    
    assert response.status_code == 403


def test_send_message_evolution_error(
    client: TestClient,
    mock_evolution_api,
    sample_outgoing_message,
    internal_auth_headers
):
    """Testa erro na Evolution API."""
    # Mock Evolution API com erro
    mock_evolution_api.post("/message/sendText").mock(
        return_value=500,  # Erro interno
        status_code=500
    )
    
    response = client.post(
        "/messages/send",
        json=sample_outgoing_message,
        headers=internal_auth_headers
    )
    
    assert response.status_code == 200  # Retorna sucesso=False
    data = response.json()
    assert data["success"] is False
    assert "error" in data


def test_send_message_with_reply(
    client: TestClient,
    mock_evolution_api,
    internal_auth_headers
):
    """Testa envio de mensagem com reply."""
    message = {
        "to": "5511999999999",
        "text": "Resposta à sua mensagem",
        "reply_to": "original_message_id"
    }
    
    # Mock Evolution API
    mock_evolution_api.post("/message/sendText").mock(
        return_value={"key": {"id": "sent_message_id"}}
    )
    
    response = client.post(
        "/messages/send",
        json=message,
        headers=internal_auth_headers
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True


def test_send_message_invalid_payload(
    client: TestClient,
    internal_auth_headers
):
    """Testa payload inválido."""
    invalid_message = {
        "to": "invalid_number",  # Número inválido
        "text": "",  # Texto vazio
    }
    
    response = client.post(
        "/messages/send",
        json=invalid_message,
        headers=internal_auth_headers
    )
    
    assert response.status_code == 422  # Erro de validação


def test_get_message_stats(
    client: TestClient,
    internal_auth_headers
):
    """Testa obtenção de estatísticas."""
    response = client.get("/messages/stats", headers=internal_auth_headers)
    
    assert response.status_code == 200
    data = response.json()
    assert "queue" in data
    assert "idempotency" in data
    assert "timestamp" in data


def test_get_message_stats_unauthorized(
    client: TestClient
):
    """Testa obtenção de estatísticas sem autorização."""
    response = client.get("/messages/stats")
    assert response.status_code == 422
