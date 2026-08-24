from processing.validator import validate_event


def test_valid_event():

    event = {
        "id": 1,
        "event_type": "login",
        "source": "web",
        "created_at": "2026-08-24T10:00:00",
    }

    valid, errors = validate_event(
        event
    )

    assert valid is True

    assert errors == []


def test_invalid_event():

    event = {
        "id": "wrong",
        "event_type": "login",
        "source": "web",
        "created_at": "2026-08-24T10:00:00",
    }

    valid, errors = validate_event(
        event
    )

    assert valid is False

    assert len(errors) > 0