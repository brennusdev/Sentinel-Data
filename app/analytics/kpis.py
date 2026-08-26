"""
Cálculo dos principais KPIs do Sentinel Data.
"""

from sqlalchemy import func

from models.event import Event
from models.processed_event import ProcessedEvent


def calculate_total_events(
    db,
) -> int:
    """
    Retorna o número total de eventos.
    """

    result = db.query(
        func.count(Event.id)
    ).scalar()

    return result or 0


def calculate_processed_events(
    db,
) -> int:
    """
    Retorna a quantidade de eventos processados.
    """

    result = db.query(
        func.count(ProcessedEvent.id)
    ).scalar()

    return result or 0


def calculate_invalid_events(
    db,
) -> int:
    """
    Retorna a quantidade de eventos inválidos.
    """

    result = db.query(
        Event
    ).filter(
        Event.processing_status == "invalid"
    ).count()

    return result


def calculate_average_quality(
    db,
) -> float:
    """
    Calcula a qualidade média dos eventos.
    """

    result = db.query(
        func.avg(
            ProcessedEvent.quality_score
        )
    ).scalar()

    if result is None:
        return 0.0

    return round(
        float(result),
        2,
    )