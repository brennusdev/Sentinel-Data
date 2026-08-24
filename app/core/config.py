"""
Configurações centrais do Sentinel Data.
"""

import os


class Settings:
    """
    Armazena as configurações da aplicação.
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

    # Endereço do Kafka.
    KAFKA_BOOTSTRAP_SERVERS: str = os.getenv(
        "KAFKA_BOOTSTRAP_SERVERS",
        "kafka:9092",
    )

    # Topic principal dos eventos.
    KAFKA_EVENTS_TOPIC: str = os.getenv(
        "KAFKA_EVENTS_TOPIC",
        "events.raw",
    )

    # Topic para eventos que falharam.
    KAFKA_DLQ_TOPIC: str = os.getenv(
        "KAFKA_DLQ_TOPIC",
        "events.dlq",
    )

    # Grupo responsável pelo processamento.
    KAFKA_CONSUMER_GROUP: str = os.getenv(
        "KAFKA_CONSUMER_GROUP",
        "sentinel-event-processors",
    )


settings = Settings()