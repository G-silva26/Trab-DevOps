from fastapi.testclient import TestClient
from src.main import app
from unittest.mock import patch

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_functest():
    response = client.get("/teste")
    assert response.status_code == 200
    assert response.json() == {"message": "DEU CERTO 👍🏻."}

def test_saudacao():
    response = client.get("/saudacao/Guilherme")
    assert response.status_code == 200
    assert response.text == '"Olá Guilherme! Bem-Vindo ao Python!!"'

def test_sorteio_numero():
    with patch("random.randint", return_value=42):
        response = client.get("/sorteio")
        assert response.status_code == 200
        assert response.json() == {"ok": True, "numero": 42}
