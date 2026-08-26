"""
Endpoint de métricas Prometheus.
"""

from fastapi import APIRouter

from prometheus_client import (
    CONTENT_TYPE_LATEST,
    generate_latest,
)

from fastapi.responses import Response


router = APIRouter(
    tags=["Metrics"],
)


@router.get(
    "/metrics",
    include_in_schema=False,
)
def metrics():
    """
    Retorna todas as métricas no formato
    esperado pelo Prometheus.
    """

    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )