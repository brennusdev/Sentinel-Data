"""
Dead Letter Queue.

Eventos que não podem ser processados após
todas as tentativas são enviados para a DLQ.
Controle de tentativas de processamento.
Política de retry com exponential backoff.
"""

import json

from kafka import KafkaProducer

from app.core.config import settings


producer = KafkaProducer(
    bootstrap_servers=(
        settings.KAFKA_BOOTSTRAP_SERVERS
    ),
MAX_RETRIES = 3

    value_serializer=lambda value: json.dumps(
        value
    ).encode("utf-8"),
)
MAX_RETRIES = 5