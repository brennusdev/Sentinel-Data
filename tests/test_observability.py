from app.observability.metrics import (
    EVENTS_PROCESSED,
)


def test_processed_metric():

    before = (
        EVENTS_PROCESSED
        ._value
        .get()
    )

    EVENTS_PROCESSED.inc()

    after = (
        EVENTS_PROCESSED
        ._value
        .get()
    )

    assert after == before + 1