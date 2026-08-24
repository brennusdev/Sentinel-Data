"""
Serviço responsável pelo fluxo de criação
e publicação de eventos.
"""

from sqlalchemy.orm import Session

from repositories.event_repository import create_event
from schemas.event import EventCreate
from streaming.producer import publish_event


def create_and_publish_event(
    db: Session,
    event_data: EventCreate,
):
    """
    Cria o evento no banco e publica
    o evento no Kafka.
    """

    # Primeiro persistimos o evento.
    event = create_event(
        db=db,
        event_data=event_data,
    )

    # Transformamos o objeto em uma estrutura
    # compatível com JSON.
    event_payload = {
        "id": event.id,
        "event_type": event.event_type,
        "user_id": event.user_id,
        "source": event.source,
        "value": event.value,
        "created_at": event.created_at.isoformat(),
    }

    # Publicamos no Kafka.
    kafka_metadata = publish_event(
        event_payload
    )

    return event, kafka_metadata