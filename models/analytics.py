"""
Modelo para armazenamento de métricas analíticas.
"""

from datetime import date, datetime

from Sqlalchemy import (
    Date,
    DateTime,
    Float,
    Integer,
    String,
)
from Sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.core.database import Base


class AnalyticsSnapshot(Base):
    """
    Representa um snapshot de métricas
    calculadas pelo Analytics Engine.
    """

    __tablename__ = "analytics_snapshots"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    metric_name: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False,
    )

    metric_date: Mapped[date] = mapped_column(
        Date,
        index=True,
        nullable=False,
    )

    metric_value: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )