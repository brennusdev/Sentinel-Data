"""
Criação dos tópicos Kafka.
"""

from kafka import KafkaAdminClient

from kafka.admin import (
    NewTopic,
)

from app.core.config import settings

from streaming.topics import (
    TOPICS,
)


admin = KafkaAdminClient(
    bootstrap_servers=(
        settings.KAFKA_BOOTSTRAP_SERVERS
    ),

    client_id="sentinel-admin",
)


def create_topics():
    """
    Cria todos os tópicos necessários.
    """

    topics = []

    for name, config in TOPICS.items():

        topics.append(
            NewTopic(
                name=name,
                num_partitions=(
                    config["partitions"]
                ),
                replication_factor=(
                    config["replication_factor"]
                ),
            )
        )

    try:

        admin.create_topics(
            new_topics=topics
        )

        print(
            "Kafka topics created."
        )

    except Exception as error:

        print(
            f"Topic creation warning: {error}"
        )


if __name__ == "__main__":

    create_topics()