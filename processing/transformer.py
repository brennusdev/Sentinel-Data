"""
Transformação e normalização de eventos.
"""


def transform_event(
    event: dict,
) -> dict:
    """
    Normaliza um evento antes de armazená-lo
    como dado processado.
    """

    transformed = event.copy()

    # Normaliza o tipo do evento.
    transformed["event_type"] = (
        transformed["event_type"]
        .strip()
        .lower()
    )

    # Normaliza a origem.
    transformed["source"] = (
        transformed["source"]
        .strip()
        .lower()
    )

    # Marca o evento como processado.
    transformed["processing_status"] = (
        "processed"
    )

    return transformed