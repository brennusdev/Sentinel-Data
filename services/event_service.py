"""
Camada de serviço responsável pelas regras
relacionadas aos eventos.
"""

from sqlalchemy.orm import Session

from repositories.event_repository import create_event
from schemas.event import EventCreate
from app.workers.event_worker import process_event


def create_and_queue_event(
    db: Session,
    event_data: EventCreate,
):
    """
    Cria um evento e envia sua identificação
    para processamento assíncrono.
    """

    # Primeiro salvamos o evento.
    event = create_event(
        db=db,
        event_data=event_data,
    )

    # Depois enviamos o ID para o worker.
    task = process_event.delay(event.id)

    return event, task.id