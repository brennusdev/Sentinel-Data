"""
Worker responsável pelo processamento assíncrono
dos eventos.
"""

from datetime import datetime

from app.core.celery import celery_app
from app.core.database import SessionLocal
from models.event import Event


@celery_app.task(
    bind=True,
    max_retries=3,
)
def process_event(
    self,
    event_id: int,
):
    """
    Processa um evento recebido pela API.
    """

    db = SessionLocal()

    try:
        # Busca o evento.
        event = db.get(Event, event_id)

        # Caso o evento não exista,
        # não existe nada para processar.
        if event is None:
            return {
                "status": "not_found",
                "event_id": event_id,
            }

        # Marca o evento como em processamento.
        event.status = "processing"

        db.commit()

        # --------------------------------------------------
        # Aqui futuramente teremos regras de processamento.
        # --------------------------------------------------

        event.status = "processed"

        event.processed_at = datetime.utcnow()

        db.commit()

        return {
            "status": "processed",
            "event_id": event_id,
        }

    except Exception as exc:

        # Incrementa a quantidade de tentativas.
        if event is not None:
            event.retry_count += 1
            event.status = "failed"

            db.commit()

        # Solicita uma nova tentativa ao Celery.
        raise self.retry(
            exc=exc,
            countdown=5,
        )

    finally:
        db.close()