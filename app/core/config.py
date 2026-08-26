"""
Configuração central da aplicação.
"""

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):

    APP_ENV: str = "development"

    DATABASE_URL: str

    KAFKA_BOOTSTRAP_SERVERS: str

    KAFKA_CONSUMER_GROUP: str = (
        "sentinel-processors"
    )

    SECRET_KEY: str

    LOG_LEVEL: str = "INFO"


    model_config = SettingsConfigDict(

        env_file=".env",

        extra="ignore",
    )


settings = Settings()