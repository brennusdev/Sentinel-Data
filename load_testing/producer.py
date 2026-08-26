"""
Gerador de carga do Sentinel Data.

Responsável por produzir grandes volumes
de eventos para testes de performance.
"""

import json
import time

from uuid import uuid4

from kafka import KafkaProducer

from app.core.config import settings


producer = KafkaProducer(

    bootstrap_servers=(
        settings.KAFKA_BOOTSTRAP_SERVERS
    ),

    value_serializer=lambda value:
        json.dumps(
            value
        ).encode("utf-8"),
)


def generate_event(
    index: int,
) -> dict:
    """
    Gera um evento sintético.
    """

    return {

        "id": str(uuid4()),

        "event_type": "page_view",

        "user_id": index,

        "timestamp": time.time(),

        "payload": {

            "page": "/dashboard",

            "source": "load-test",
        },
    }


def generate_events(
    total: int,
):
    """
    Produz uma quantidade definida
    de eventos no Kafka.
    """

    start = time.perf_counter()

    for index in range(total):

        event = generate_event(
            index
        )

        producer.send(
            settings.KAFKA_EVENTS_TOPIC,

            value=event,
        )

    producer.flush()

    elapsed = (
        time.perf_counter()
        - start
    )

    throughput = (
        total / elapsed
        if elapsed > 0
        else 0
    )

    print(
        f"Events: {total}"
    )

    print(
        f"Time: {elapsed:.2f}s"
    )

    print(
        f"Throughput: {throughput:.2f} events/s"
    )


if __name__ == "__main__":

    generate_events(
        total=100_000
    )