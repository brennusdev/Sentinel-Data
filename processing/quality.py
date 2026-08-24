"""
Cálculo de qualidade dos dados.
"""


def calculate_quality_score(
    event: dict,
    errors: list[str],
) -> float:
    """
    Calcula um score simples de qualidade.

    100 = excelente
    0   = inválido
    """

    if errors:
        return 0.0

    score = 100.0

    # Eventos sem usuário recebem uma pequena
    # penalização porque algumas análises
    # podem depender dessa informação.
    if event.get("user_id") is None:

        score -= 10.0

    # Eventos sem valor também podem ser menos
    # úteis para análises financeiras.
    if (
        event["event_type"]
        in {"purchase", "payment"}
        and event.get("value") is None
    ):

        score -= 30.0

    return max(score, 0.0)