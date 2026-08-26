"""
Acesso aos dados analíticos.
"""

from datetime import date

from models.analytics import (
    AnalyticsSnapshot,
)


def save_metric(
    db,
    metric_name: str,
    metric_date: date,
    metric_value: float,
):
    """
    Salva uma métrica calculada.
    """

    snapshot = AnalyticsSnapshot(
        metric_name=metric_name,
        metric_date=metric_date,
        metric_value=metric_value,
    )

    db.add(snapshot)

    db.commit()

    db.refresh(snapshot)

    return snapshot