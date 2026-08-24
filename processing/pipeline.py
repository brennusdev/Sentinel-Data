"""
Pipeline central de processamento de dados.
"""

from processing.quality import (
    calculate_quality_score,
)

from processing.transformer import (
    transform_event,
)

from processing.validator import (
    validate_event,
)


def process_event(
    event: dict,
) -> dict:
    """
    Executa o pipeline completo.

    Fluxo:

    Input
      ↓
    Validation
      ↓
    Transformation
      ↓
    Quality
      ↓
    Output
    """

    # ---------------------------
    # 1. Validation
    # ---------------------------

    is_valid, errors = validate_event(
        event
    )

    # Calcula a qualidade.
    quality_score = calculate_quality_score(
        event,
        errors,
    )

    # Evento inválido.
    if not is_valid:

        return {
            "status": "invalid",
            "quality_score": quality_score,
            "errors": errors,
            "data": event,
        }

    # ---------------------------
    # 2. Transformation
    # ---------------------------

    transformed = transform_event(
        event
    )

    # ---------------------------
    # 3. Resultado
    # ---------------------------

    return {
        "status": "processed",
        "quality_score": quality_score,
        "errors": [],
        "data": transformed,
    }