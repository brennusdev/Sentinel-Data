"""
Aplicação principal do Sentinel Data.
"""

from fastapi import FastAPI

from app.api.routes.analytics import (
    router as analytics_router,
)

from app.api.routes.events import (
    router as events_router,
)


app = FastAPI(
    title="Sentinel Data",
    version="5.0.0",
    description=(
        "Real-time data ingestion, "
        "processing and analytics platform."
    ),
)


app.include_router(
    events_router
)

app.include_router(
    analytics_router
)


@app.get("/health")
def health():
    """
    Health check da aplicação.
    """

    return {
        "status": "healthy",
        "version": "5.0.0",
    }