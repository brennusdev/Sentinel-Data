from processing.aggregator import (
    aggregate_events,
)


def test_aggregate_events():

    events = [
        {
            "event_type": "login",
        },
        {
            "event_type": "login",
        },
        {
            "event_type": "purchase",
        },
    ]

    result = aggregate_events(
        events
    )

    assert result[0]["event_type"] == "login"

    assert result[0]["event_count"] == 2