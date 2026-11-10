from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "mensagem": "Olá Kubernetes!"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }