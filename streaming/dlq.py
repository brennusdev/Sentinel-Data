"""
Dead Letter Queue.

Eventos que não podem ser processados após
todas as tentativas são enviados para a DLQ.
"""

import json

from kafka import KafkaProducer

from app.core.config import settings


producer = KafkaProducer(
    bootstrap_servers=(
        settings.KAFKA_BOOTSTRAP_SERVERS
    ),

    value_serializer=lambda value: json.dumps(
        value
    ).encode("utf-8"),
)


def send_to_dlq(
    event: dict,
    error: str,
):
    """
    Envia um evento problemático para a DLQ.
    """

    payload = {
        "event": event,

        "error": error,

        "reason": "processing_failed",
    }

    producer.send(
        settings.KAFKA_DLQ_TOPIC,
        value=payload,
    )

    producer.flush()