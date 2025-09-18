from src.app import *
from unittest.mock import patch

def test_root():
    assert root() == {"message": "Hello World"}

def test_functest():
    assert functest() == {"message": "DEU CERTO 👍🏻."}

def test_saudacao():
    assert saudacao("Guilherme") == "Olá Guilherme! Bem-Vindo ao Python!!"

def test_numero_aleatorio():
    with patch("random.randint", return_value=777):
        from random import randint
        numero = randint(1, 1000)
        assert numero == 777
