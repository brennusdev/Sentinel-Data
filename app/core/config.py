"""
Configurações da aplicação.
"""

import os


class Settings:
    """
    Configurações centrais do Sentinel Data.
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

    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0",
    )


settings = Settings()