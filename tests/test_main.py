import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import app
from fastapi.testclient import TestClient
from unittest.mock import patch
import random
import pytest

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_saudacao():
    response = client.get("/saudacao/Guilherme")
    assert response.status_code == 200
    assert response.text == '"Olá Guilherme! Bem-Vindo ao Python!!"'

def test_sorteio_numero():
    with patch("random.randint", return_value=42):
        response = client.get("/sorteio")
        assert response.status_code == 200
        assert response.json() == {"ok": True, "numero": 42}

def test_root_content_type():
    response = client.get("/")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

@pytest.mark.parametrize("nome, esperado", [
    ("Guilherme", "Olá Guilherme! Bem-Vindo ao Python!!"),
    ("Felipe", "Olá Felipe! Bem-Vindo ao Python!!"),
    ("Aline", "Olá Aline! Bem-Vindo ao Python!!")
])
def test_saudacao_varios_nomes(nome, esperado):
    response = client.get(f"/saudacao/{nome}")
    assert response.status_code == 200
    assert response.text == f'"{esperado}"'

