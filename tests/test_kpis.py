from unittest.mock import MagicMock, patch

from app.analytics.kpis import (
    calculate_average_quality,
)


@patch(
    "app.analytics.kpis.func"
)
def test_average_quality(mock_func):

    db = MagicMock()

    result_query = MagicMock()

    result_query.scalar.return_value = 95.5

    db.query.return_value = result_query

    result = calculate_average_quality(
        db
    )

    assert result == 95.5