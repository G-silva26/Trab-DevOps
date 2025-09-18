from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def functest():
    return {"message": "DEU CERTO 👍🏻."}

@app.get("/saudacao/{nome}")
async def saudacao(nome: str):
    return f"Olá {nome}! Bem-Vindo ao Python!!"

@app.get("/sorteio")
async def sorteio_numero():
    numero = random.randint(1, 100)
    return {"ok": True, "numero": numero}
