"""
Configurações centrais do Sentinel Data.
"""

import os


class Settings:
    """
    Armazena configurações da aplicação.
    """

    APP_NAME: str = os.getenv(
        "APP_NAME",
        "Sentinel Data",
    )

    ENVIRONMENT: str = os.getenv(
        "ENVIRONMENT",
        "development",
    )

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://sentinel:sentinel@localhost:5432/sentinel",
    )

    KAFKA_BOOTSTRAP_SERVERS: str = os.getenv(
        "KAFKA_BOOTSTRAP_SERVERS",
        "kafka:9092",
    )

    KAFKA_EVENTS_TOPIC: str = os.getenv(
        "KAFKA_EVENTS_TOPIC",
        "events.raw",
    )

    KAFKA_PROCESSED_TOPIC: str = os.getenv(
        "KAFKA_PROCESSED_TOPIC",
        "events.processed",
    )

    KAFKA_INVALID_TOPIC: str = os.getenv(
        "KAFKA_INVALID_TOPIC",
        "events.invalid",
    )

    KAFKA_DLQ_TOPIC: str = os.getenv(
        "KAFKA_DLQ_TOPIC",
        "events.dlq",
    )

    KAFKA_CONSUMER_GROUP: str = os.getenv(
        "KAFKA_CONSUMER_GROUP",
        "sentinel-event-processors",
    )


settings = Settings()