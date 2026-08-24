"""
Endpoint responsável pelo health check da aplicação.
"""

from fastapi import APIRouter


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    """
    Verifica se a API está funcionando.
    """

    return {
        "status": "healthy",
        "service": "sentinel-data",
    }