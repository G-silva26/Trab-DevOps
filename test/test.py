from src.main import *
from unittest.mock import patch

def test_root():
    assert root() == {"message": "Hello World"}

def test_functest():
    assert functest() == {"message": "DEU CERTO 👍🏻."}

def test_saudacao():
    assert saudacao("Guilherme") == "Olá Guilherme! Bem-Vindo ao Python!!"

def test_sorteio_numero():
    with patch("random.randint", return_value=42):
        resultado = sorteio_numero()
        assert resultado == {"ok": True, "numero": 42}
