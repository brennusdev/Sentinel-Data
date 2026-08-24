"""
Validação dos eventos recebidos pelo Sentinel Data.
"""


REQUIRED_FIELDS = {
    "id",
    "event_type",
    "source",
    "created_at",
}


def validate_event(
    event: dict,
) -> tuple[bool, list[str]]:
    """
    Valida um evento recebido.

    Retorna:

    (True, [])
    
    quando o evento é válido.

    Ou:

    (False, [...])

    quando existem erros.
    """

    errors = []

    # Verifica campos obrigatórios.
    for field in REQUIRED_FIELDS:

        if field not in event:
            errors.append(
                f"Missing required field: {field}"
            )

    # Não precisamos continuar se faltarem
    # campos fundamentais.
    if errors:
        return False, errors

    # Verifica o tipo do ID.
    if not isinstance(event["id"], int):

        errors.append(
            "Field 'id' must be an integer"
        )

    # Verifica event_type.
    if not isinstance(
        event["event_type"],
        str,
    ):
        errors.append(
            "Field 'event_type' must be a string"
        )

    # Verifica source.
    if not isinstance(
        event["source"],
        str,
    ):
        errors.append(
            "Field 'source' must be a string"
        )

    return len(errors) == 0, errors