"""
Analytics Engine principal.
"""

from app.analytics.kpis import (
    calculate_average_quality,
    calculate_processed_events,
    calculate_total_events,
)


def generate_kpis(
    db,
) -> dict:
    """
    Gera o conjunto principal de KPIs.
    """

    total_events = calculate_total_events(
        db
    )

    processed_events = calculate_processed_events(
        db
    )

    average_quality = calculate_average_quality(
        db
    )

    return {
        "total_events": total_events,

        "processed_events": processed_events,

        "invalid_events": (
            total_events - processed_events
        ),

        "average_quality_score": (
            average_quality
        ),

        # Será implementado na próxima etapa.
        "unique_users": 0,
    }