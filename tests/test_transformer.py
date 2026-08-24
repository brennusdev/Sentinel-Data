from processing.transformer import (
    transform_event,
)


def test_transform_event():

    event = {
        "id": 1,
        "event_type": " PURCHASE ",
        "source": " WEB ",
    }

    result = transform_event(
        event
    )

    assert result["event_type"] == "purchase"

    assert result["source"] == "web"

    assert (
        result["processing_status"]
        == "processed"
    )