"""Testes para gerenciamento de instâncias."""
import pytest
from fastapi.testclient import TestClient
import respx

from app.config import settings


def test_ensure_instance_success(
    client: TestClient,
    mock_evolution_api,
    internal_auth_headers
):
    """Testa criação/verificação bem-sucedida de instância."""
    # Mock Evolution API - instância não existe
    mock_evolution_api.get(f"/instance/fetch/{settings.evolution_instance_name}").mock(
        return_value=404,  # Não encontrada
        status_code=404
    )
    
    # Mock criação
    mock_evolution_api.post("/instance/create").mock(
        return_value={"instance": {"instanceName": settings.evolution_instance_name}}
    )
    
    # Mock start
    mock_evolution_api.post("/instance/start").mock(
        return_value={"status": "starting"}
    )
    
    response = client.post("/instance/ensure", headers=internal_auth_headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == settings.evolution_instance_name
    assert data["status"] == "starting"
    assert data["connected"] is False


def test_ensure_instance_already_exists(
    client: TestClient,
    mock_evolution_api,
    internal_auth_headers
):
    """Testa instância que já existe e está conectada."""
    # Mock Evolution API - instância existe e conectada
    mock_evolution_api.get(f"/instance/fetch/{settings.evolution_instance_name}").mock(
        return_value={
            "instance": {
                "instanceName": settings.evolution_instance_name,
                "status": "open"
            }
        }
    )
    
    response = client.post("/instance/ensure", headers=internal_auth_headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == settings.evolution_instance_name
    assert data["status"] == "open"
    assert data["connected"] is True


def test_ensure_instance_needs_start(
    client: TestClient,
    mock_evolution_api,
    internal_auth_headers
):
    """Testa instância que existe mas precisa ser iniciada."""
    # Mock Evolution API - instância existe mas offline
    mock_evolution_api.get(f"/instance/fetch/{settings.evolution_instance_name}").mock(
        return_value={
            "instance": {
                "instanceName": settings.evolution_instance_name,
                "status": "close"
            }
        }
    )
    
    # Mock start
    mock_evolution_api.post("/instance/start").mock(
        return_value={"status": "starting"}
    )
    
    response = client.post("/instance/ensure", headers=internal_auth_headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "starting"
    assert data["connected"] is False


def test_ensure_instance_unauthorized(
    client: TestClient
):
    """Testa criação de instância sem autorização."""
    response = client.post("/instance/ensure")
    assert response.status_code == 422


def test_get_qr_code_success(
    client: TestClient,
    mock_evolution_api,
    internal_auth_headers
):
    """Testa obtenção bem-sucedida de QR code."""
    # Mock Evolution API
    mock_evolution_api.get(f"/instance/connect/{settings.evolution_instance_name}").mock(
        return_value={"qrcode": "base64_encoded_qr_code"}
    )
    
    response = client.get("/instance/qr", headers=internal_auth_headers)
    
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Conecte seu WhatsApp" in response.text
    assert "base64_encoded_qr_code" in response.text


def test_get_qr_code_not_available(
    client: TestClient,
    mock_evolution_api,
    internal_auth_headers
):
    """Testa QR code não disponível."""
    # Mock Evolution API - QR não disponível
    mock_evolution_api.get(f"/instance/connect/{settings.evolution_instance_name}").mock(
        return_value=404,  # Não encontrado
        status_code=404
    )
    
    response = client.get("/instance/qr", headers=internal_auth_headers)
    
    assert response.status_code == 404
    assert "QR Code não disponível" in response.text


def test_get_qr_code_unauthorized(
    client: TestClient
):
    """Testa obtenção de QR code sem autorização."""
    response = client.get("/instance/qr")
    assert response.status_code == 422


def test_get_instance_status_success(
    client: TestClient,
    mock_evolution_api,
    internal_auth_headers
):
    """Testa obtenção bem-sucedida de status da instância."""
    # Mock Evolution API
    mock_evolution_api.get(f"/instance/fetch/{settings.evolution_instance_name}").mock(
        return_value={
            "instance": {
                "instanceName": settings.evolution_instance_name,
                "status": "open"
            }
        }
    )
    
    response = client.get("/instance/status", headers=internal_auth_headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == settings.evolution_instance_name
    assert data["status"] == "open"
    assert data["connected"] is True


def test_get_instance_status_not_found(
    client: TestClient,
    mock_evolution_api,
    internal_auth_headers
):
    """Testa instância não encontrada."""
    # Mock Evolution API - instância não existe
    mock_evolution_api.get(f"/instance/fetch/{settings.evolution_instance_name}").mock(
        return_value=404,  # Não encontrada
        status_code=404
    )
    
    response = client.get("/instance/status", headers=internal_auth_headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "not_found"
    assert data["connected"] is False
    assert "error" in data


def test_get_instance_status_unauthorized(
    client: TestClient
):
    """Testa obtenção de status sem autorização."""
    response = client.get("/instance/status")
    assert response.status_code == 422
