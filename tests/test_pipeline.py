from processing.pipeline import (
    process_event,
)


def test_pipeline():

    event = {
        "id": 1,
        "event_type": " PURCHASE ",
        "source": " WEB ",
        "created_at": "2026-08-24T10:00:00",
        "user_id": 100,
        "value": 199.90,
    }

    result = process_event(
        event
    )

    assert result["status"] == "processed"

    assert result["quality_score"] == 100.0

    assert (
        result["data"]["event_type"]
        == "purchase"
    )