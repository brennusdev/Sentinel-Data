"""
Testes relacionados ao streaming.
"""

from unittest.mock import MagicMock, patch

from streaming.producer import publish_event


@patch(
    "app.streaming.producer.producer.send"
)
def test_publish_event(mock_send):
    """
    Verifica se o producer publica
    corretamente um evento.
    """

    metadata = MagicMock()

    metadata.topic = "events.raw"
    metadata.partition = 0
    metadata.offset = 10

    mock_future = MagicMock()

    mock_future.get.return_value = metadata

    mock_send.return_value = mock_future

    event = {
        "id": 1,
        "event_type": "login",
        "user_id": 10,
        "source": "web",
        "value": None,
    }

    result = publish_event(event)

    assert result["topic"] == "events.raw"

    assert result["partition"] == 0

    assert result["offset"] == 10

    mock_send.assert_called_once()