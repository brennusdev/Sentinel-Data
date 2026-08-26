"""
Pipeline principal de processamento do Sentinel Data.

Responsável por coordenar as etapas de processamento
dos eventos recebidos pelo sistema.
"""

from processing.validator import validate_event
from processing.transformer import transform_event
from processing.quality import calculate_quality


def process_event(
    event: dict,
) -> dict:
    """
    Processa um único evento.

    Fluxo:

    1. Valida o evento.
    2. Transforma os dados.
    3. Calcula a qualidade.
    4. Retorna o evento processado.
    """

    # ========================================================
    # 1. VALIDAÇÃO
    # ========================================================

    validated_event = validate_event(
        event
    )

    # Se o evento não for válido,
    # interrompemos o processamento.
    if not validated_event:

        raise ValueError(
            "Evento inválido."
        )

    # ========================================================
    # 2. TRANSFORMAÇÃO
    # ========================================================

    transformed_event = transform_event(
        event
    )

    # ========================================================
    # 3. QUALIDADE
    # ========================================================

    quality_score = calculate_quality(
        transformed_event
    )

    # ========================================================
    # 4. RESULTADO
    # ========================================================

    return {
        **transformed_event,
        "quality_score": quality_score,
    }


def process_batch(
    events: list[dict],
) -> list[dict]:
    """
    Processa múltiplos eventos em lote.

    Parameters
    ----------
    events:
        Lista de eventos recebidos.

    Returns
    -------
    list[dict]
        Lista de eventos processados.
    """

    # Lista que armazenará os resultados.
    results = []

    # Percorre cada evento recebido.
    for event in events:

        try:

            # Processa individualmente o evento.
            result = process_event(
                event
            )

            # Adiciona o resultado
            # à lista final.
            results.append(
                result
            )

        except Exception as error:

            # Em uma arquitetura real,
            # esse erro deverá ser encaminhado
            # para o sistema de retry/DLQ.
            print(
                f"Erro ao processar evento: {error}"
            )

    # Retorna todos os eventos processados.
    return results