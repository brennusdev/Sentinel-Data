"""
Schemas relacionados aos eventos.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class EventCreate(BaseModel):
    """
    Dados necessários para criar um evento.
    """

    event_type: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )

    user_id: int | None = None

    source: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )

    value: float | None = Field(
        default=None,
        ge=0,
    )


class EventResponse(BaseModel):
    """
    Resposta da API.
    """

    id: int
    event_type: str
    user_id: int | None
    source: str
    value: float | None

    status: str

    retry_count: int

    created_at: datetime

    processed_at: datetime | None

    class Config:
        from_attributes = True


class EventQueuedResponse(BaseModel):
    """
    Resposta enviada quando um evento
    é colocado na fila.
    """

    event_id: int

    task_id: str

    status: str