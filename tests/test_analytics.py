from unittest.mock import MagicMock

from app.analytics.rankings import (
    get_event_ranking,
)


def test_event_ranking():

    db = MagicMock()

    query = MagicMock()

    query.group_by.return_value = query

    query.order_by.return_value = query

    query.limit.return_value = query

    query.all.return_value = [
        ("login", 100),
        ("purchase", 50),
    ]

    db.query.return_value = query

    result = get_event_ranking(
        db,
        limit=10,
    )

    assert result[0]["event_type"] == "login"

    assert result[0]["count"] == 100