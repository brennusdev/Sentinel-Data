"""
Modelo responsável pelos eventos processados.
"""

from datetime import datetime

from sqlalchemy import (
    DateTime,
    Float,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.core.database import Base


class ProcessedEvent(Base):
    """
    Representa um evento depois do processamento.
    """

    __tablename__ = "processed_events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    original_event_id: Mapped[int] = mapped_column(
        Integer,
        index=True,
        nullable=False,
    )

    event_type: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False,
    )

    source: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    quality_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    processing_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    errors: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    processed_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )