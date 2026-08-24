"""
Testes básicos da API do Sentinel Data.
"""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    """
    Verifica se a API principal está funcionando.
    """

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "Sentinel Data"
    assert data["version"] == "1.0.0"


def test_health():
    """
    Verifica o health check.
    """

    response = client.get("/health/")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"