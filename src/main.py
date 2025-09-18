from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def functest():
    return {"message": "DEU CERTO 👍🏻."}

def root():
    return {"message": "Hello World"}

def functest():
    return {"message": "DEU CERTO 👍🏻."}

def saudacao(nome):
    return f"Olá {nome}! Bem-Vindo ao Python!!"

def sorteio_numero():
    numero = random.randint(1, 100)
    return {"ok": True, "numero": numero}
