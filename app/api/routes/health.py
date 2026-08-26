"""
Endpoints de saúde da aplicação.
"""

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.core.database import (
    get_db,
)

from observability.health import (
    check_database,
)


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/live")
def liveness():

    return {
        "status": "alive",
    }


@router.get("/ready")
def readiness(
    db: Session = Depends(get_db),
):

    database_available = (
        check_database(db)
    )

    if not database_available:

        return {
            "status": "not_ready",
            "database": "down",
        }

    return {
        "status": "ready",
        "database": "up",
    }