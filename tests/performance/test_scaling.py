"""
Testes conceituais de escalabilidade.
"""

from load_testing.benchmark import (
    calculate_throughput,
)


def test_throughput():

    throughput = calculate_throughput(
        total_events=10_000,
        elapsed_seconds=20,
    )

    assert throughput == 500


def test_zero_time():

    throughput = calculate_throughput(
        total_events=10_000,
        elapsed_seconds=0,
    )

    assert throughput == 0