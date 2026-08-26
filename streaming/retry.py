"""
Controle de tentativas de processamento.
"""

MAX_RETRIES = 3


def should_retry(
    retry_count: int,
) -> bool:
    """
    Determina se o evento ainda pode ser
    processado novamente.
    """

    return retry_count < MAX_RETRIES


def next_retry_count(
    retry_count: int,
) -> int:
    """
    Incrementa o contador de tentativas.
    """

    return retry_count + 1