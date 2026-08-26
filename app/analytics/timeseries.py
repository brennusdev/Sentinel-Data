"""
Séries temporais de eventos.
"""

from sqlalchemy import func

from models.processed_event import (
    ProcessedEvent,
)


def get_hourly_events(
    db,
) -> list[dict]:
    """
    Agrupa eventos por hora.
    """

    results = (
        db.query(
            func.date_trunc(
                "hour",
                ProcessedEvent.processed_at,
            ).label("timestamp"),

            func.count(
                ProcessedEvent.id
            ).label("value"),
        )
        .group_by(
            "timestamp"
        )
        .order_by(
            "timestamp"
        )
        .all()
    )

    return [
        {
            "timestamp": timestamp.isoformat(),
            "value": value,
        }
        for timestamp, value in results
    ]