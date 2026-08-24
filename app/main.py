"""
Ponto de entrada principal do Sentinel Data.
"""

from fastapi import FastAPI

from app.api.routes.events import router as events_router
from app.api.routes.health import router as health_router
from app.core.config import settings


# Criação da aplicação FastAPI.
app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "Plataforma de ingestão e análise "
        "de eventos em tempo real."
    ),
    version="1.0.0",
)


# Registro das rotas.
app.include_router(health_router)
app.include_router(events_router)


@app.get("/")
def root():
    """
    Endpoint inicial da aplicação.
    """

    return {
        "application": settings.APP_NAME,
        "version": "1.0.0",
        "status": "running",
    }