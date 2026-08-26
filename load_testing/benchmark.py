"""
Benchmark básico do Sentinel Data.
"""

from dataclasses import dataclass


@dataclass
class BenchmarkResult:
    """
    Resultado de um teste de carga.
    """

    total_events: int

    elapsed_seconds: float

    throughput: float

    successful_events: int

    failed_events: int

    error_rate: float


def calculate_throughput(
    total_events: int,
    elapsed_seconds: float,
) -> float:
    """
    Calcula eventos processados por segundo.
    """

    if elapsed_seconds <= 0:

        return 0.0

    return (
        total_events
        / elapsed_seconds
    )


def calculate_error_rate(
    failed_events: int,
    total_events: int,
) -> float:
    """
    Calcula percentual de erros.
    """

    if total_events <= 0:

        return 0.0

    return (
        failed_events
        / total_events
    ) * 100