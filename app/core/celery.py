"""
Configuração do Celery.

O Celery será responsável por enviar tarefas
para processamento assíncrono.
"""

from celery import Celery

from app.core.config import settings


celery_app = Celery(
    "sentinel_data",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)


celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)