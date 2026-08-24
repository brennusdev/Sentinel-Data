"""
Kafka Producer responsável por publicar eventos.
"""

import json

from kafka import KafkaProducer

from app.core.config import settings


producer = KafkaProducer(
    bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,

    # Serializa os valores para JSON.
    value_serializer=lambda value: json.dumps(
        value
    ).encode("utf-8"),

    # Serializa a chave como string.
    key_serializer=lambda key: key.encode("utf-8")
    if key
    else None,
)


def publish_event(
    event: dict,
):
    """
    Publica um evento no Kafka.

    A chave do evento utiliza o ID para manter
    uma identificação consistente dentro do Kafka.
    """

    event_id = str(event["id"])

    future = producer.send(
        settings.KAFKA_EVENTS_TOPIC,
        key=event_id,
        value=event,
    )

    # Aguarda confirmação do broker.
    metadata = future.get(
        timeout=10
    )

    return {
        "topic": metadata.topic,
        "partition": metadata.partition,
        "offset": metadata.offset,
    }