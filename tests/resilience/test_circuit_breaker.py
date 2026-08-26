from app.core.resilience import (
    CircuitBreaker,
)


def test_circuit_starts_closed():

    breaker = CircuitBreaker()

    assert (
        breaker.state
        == "CLOSED"
    )


def test_circuit_opens_after_failures():

    breaker = CircuitBreaker(
        failure_threshold=3,
    )

    breaker.record_failure()

    breaker.record_failure()

    breaker.record_failure()

    assert (
        breaker.state
        == "OPEN"
    )


def test_open_circuit_blocks_request():

    breaker = CircuitBreaker(
        failure_threshold=1,
    )

    breaker.record_failure()

    assert (
        breaker.allow_request()
        is False
    )