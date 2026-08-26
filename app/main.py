"""
Aplicação principal do Sentinel Data V6.
"""

from fastapi import FastAPI

from app.api.routes.analytics import (
    router as analytics_router,
)

from app.api.routes.events import (
    router as events_router,
)

from app.api.routes.metrics import (
    router as metrics_router,
)


app = FastAPI(
    title="Sentinel Data",
    version="6.0.0",
    description=(
        "Real-time data ingestion, "
        "processing, analytics "
        "and observability platform."
    ),
)


app.include_router(
    events_router
)

app.include_router(
    analytics_router
)

app.include_router(
    metrics_router
)


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "version": "6.0.0",
    }