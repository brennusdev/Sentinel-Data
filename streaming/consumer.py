"""
Consumer responsável por consumir eventos
e executar o pipeline de processamento.
"""

import json

from kafka import KafkaConsumer, KafkaProducer

from app.core.config import settings
from processing.pipeline import (
    process_event,
)


consumer = KafkaConsumer(
    settings.KAFKA_EVENTS_TOPIC,

    bootstrap_servers=(
        settings.KAFKA_BOOTSTRAP_SERVERS
    ),

    group_id=(
        settings.KAFKA_CONSUMER_GROUP
    ),

    auto_offset_reset="earliest",

    enable_auto_commit=False,

    value_deserializer=lambda value: json.loads(
        value.decode("utf-8")
    ),
)


producer = KafkaProducer(
    bootstrap_servers=(
        settings.KAFKA_BOOTSTRAP_SERVERS
    ),

    value_serializer=lambda value: json.dumps(
        value
    ).encode("utf-8"),
)


def publish_processed_event(
    result: dict,
):
    """
    Publica o resultado do processamento
    no tópico apropriado.
    """

    if result["status"] == "processed":

        producer.send(
            settings.KAFKA_PROCESSED_TOPIC,
            value=result,
        )

    else:

        producer.send(
            settings.KAFKA_INVALID_TOPIC,
            value=result,
        )

    producer.flush()


def run_consumer():
    """
    Loop principal do consumidor.
    """

    print(
        "Sentinel Data V4 Processor iniciado."
    )

    for message in consumer:

        try:

            event = message.value

            print(
                f"Processando evento "
                f"{event.get('id')}"
            )

            result = process_event(
                event
            )

            publish_processed_event(
                result
            )

            consumer.commit()

            print(
                f"Evento {event.get('id')} "
                f"processado: "
                f"{result['status']}"
            )

        except Exception as error:

            print(
                f"Erro no processamento: "
                f"{error}"
            )


if __name__ == "__main__":
    run_consumer()