"""
Configurações centrais do Sentinel Data.
"""

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    """
    Configurações carregadas através
    das variáveis de ambiente.
    """

    APP_ENV: str = "development"

    LOG_LEVEL: str = "INFO"

    DATABASE_URL: str

    KAFKA_BOOTSTRAP_SERVERS: str

    KAFKA_EVENTS_TOPIC: str

    KAFKA_CONSUMER_GROUP: str

    SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()