"""
Worker de processamento do Sentinel Data.

Múltiplas instâncias deste processo podem
ser executadas simultaneamente utilizando
o mesmo consumer group.
"""

import json

from kafka import KafkaConsumer

from app.core.config import settings

from processing.pipeline import (
    process_event,
)


def create_consumer():
    """
    Cria um consumer pertencente ao
    consumer group do Sentinel.
    """

    return KafkaConsumer(

        settings.KAFKA_EVENTS_TOPIC,

        bootstrap_servers=(
            settings.KAFKA_BOOTSTRAP_SERVERS
        ),

        group_id=(
            settings.KAFKA_CONSUMER_GROUP
        ),

        enable_auto_commit=False,

        auto_offset_reset="earliest",

        max_poll_records=100,

        value_deserializer=lambda value:
            json.loads(
                value.decode("utf-8")
            ),
    )


def run():

    consumer = create_consumer()

    for message in consumer:

        event = message.value

        result = process_event(
            event
        )

        print(
            f"Processed: {result}"
        )

        consumer.commit()


if __name__ == "__main__":

    run()