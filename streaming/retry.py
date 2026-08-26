"""
Política de retry com exponential backoff.
"""


MAX_RETRIES = 5


def should_retry(
    retry_count: int,
) -> bool:

    return (
        retry_count
        < MAX_RETRIES
    )


def calculate_backoff(
    retry_count: int,
) -> int:
    """
    Calcula o atraso em segundos.
    """

    return 2 ** retry_count