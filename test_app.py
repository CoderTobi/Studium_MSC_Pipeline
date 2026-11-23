from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_xy():
    assert True

def test_yz():
    assert True


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_health_ohne_datenbank(monkeypatch):
    # Port 1: dort läuft garantiert keine Datenbank
    monkeypatch.setenv("DATABASE_URL", "postgresql://postgres@localhost:1/postgres")
    response = client.get("/health")
    assert response.status_code == 503
