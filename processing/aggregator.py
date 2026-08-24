"""
Agregações utilizando Polars.
"""

import polars as pl


def aggregate_events(
    events: list[dict],
) -> list[dict]:
    """
    Agrupa eventos por tipo.

    Exemplo:

    login     → 120
    purchase  → 80
    logout    → 40
    """

    if not events:
        return []

    dataframe = pl.DataFrame(events)

    result = (
        dataframe
        .group_by("event_type")
        .agg(
            pl.len().alias("event_count")
        )
        .sort(
            "event_count",
            descending=True,
        )
    )

    return result.to_dicts()