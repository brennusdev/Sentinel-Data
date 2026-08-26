"""
Rankings analíticos.
"""

from sqlalchemy import func

from models.processed_event import (
    ProcessedEvent,
)


def get_event_ranking(
    db,
    limit: int = 10,
) -> list[dict]:
    """
    Retorna os tipos de eventos mais frequentes.
    """

    results = (
        db.query(
            ProcessedEvent.event_type,
            func.count(
                ProcessedEvent.id
            ).label("count"),
        )
        .group_by(
            ProcessedEvent.event_type
        )
        .order_by(
            func.count(
                ProcessedEvent.id
            ).desc()
        )
        .limit(limit)
        .all()
    )

    return [
        {
            "event_type": event_type,
            "count": count,
        }
        for event_type, count in results
    ]