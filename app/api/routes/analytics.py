"""
Endpoints de Analytics.
"""

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

from app.analytics.engine import (
    generate_kpis,
)

from app.analytics.rankings import (
    get_event_ranking,
)

from app.analytics.timeseries import (
    get_hourly_events,
)

from app.core.database import (
    get_db,
)


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/kpis")
def get_kpis(
    db: Session = Depends(get_db),
):
    """
    Retorna os principais KPIs.
    """

    return generate_kpis(
        db
    )


@router.get("/ranking")
def event_ranking(
    db: Session = Depends(get_db),
):
    """
    Retorna ranking dos eventos.
    """

    return get_event_ranking(
        db
    )


@router.get("/timeseries")
def event_timeseries(
    db: Session = Depends(get_db),
):
    """
    Retorna eventos agrupados por hora.
    """

    return get_hourly_events(
        db
    )