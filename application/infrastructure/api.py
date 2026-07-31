# Capa de Infraestructura - Puerta de Entrada FastAPI
from fastapi import FastAPI

app = FastAPI(title="SILRED Inteligencia Logística", version="1.0.0")

@app.get("/")
def inicio():
    return {"estado": "Operacional", "plataforma": "SILRED"}

@app.get("/alertas")
def obtener_alertas():
    return {"mensaje": "No hay alertas críticas en este sector"}

