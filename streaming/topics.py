"""
Tópicos Kafka utilizados pelo Sentinel Data.
"""

from app.core.config import settings


RAW_EVENTS_TOPIC = settings.KAFKA_EVENTS_TOPIC

PROCESSED_EVENTS_TOPIC = (
    settings.KAFKA_PROCESSED_TOPIC
)

INVALID_EVENTS_TOPIC = (
    settings.KAFKA_INVALID_TOPIC
)

DLQ_TOPIC = settings.KAFKA_DLQ_TOPIC

CONSUMER_GROUP = settings.KAFKA_CONSUMER_GROUP