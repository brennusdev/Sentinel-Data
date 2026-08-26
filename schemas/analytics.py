"""
Schemas utilizados pelos endpoints de analytics.
"""

from datetime import date

from pydantic import BaseModel


class MetricResponse(BaseModel):
    """
    Representa uma métrica individual.
    """

    metric_name: str

    metric_date: date

    metric_value: float


class KPIResponse(BaseModel):
    """
    KPIs principais da plataforma.
    """

    total_events: int

    processed_events: int

    invalid_events: int

    average_quality_score: float

    unique_users: int


class EventRanking(BaseModel):
    """
    Ranking de tipos de eventos.
    """

    event_type: str

    count: int


class TimeSeriesPoint(BaseModel):
    """
    Ponto de uma série temporal.
    """

    timestamp: str

    value: int