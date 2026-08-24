"""
Definição dos tópicos Kafka utilizados
pelo Sentinel Data.
"""

from app.core.config import settings


EVENTS_TOPIC = settings.KAFKA_EVENTS_TOPIC

DLQ_TOPIC = settings.KAFKA_DLQ_TOPIC

CONSUMER_GROUP = settings.KAFKA_CONSUMER_GROUP