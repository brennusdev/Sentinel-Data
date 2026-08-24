"""
Repository responsável pela persistência
dos eventos.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.event import Event
from schemas.event import EventCreate


def create_event(
    db: Session,
    event_data: EventCreate,
) -> Event:
    """
    Cria um evento no banco.
    """

    event = Event(
        event_type=event_data.event_type,
        user_id=event_data.user_id,
        source=event_data.source,
        value=event_data.value,
        status="pending",
    )

    db.add(event)

    db.commit()

    db.refresh(event)

    return event


def get_events(
    db: Session,
) -> list[Event]:
    """
    Retorna todos os eventos.
    """

    query = select(Event).order_by(
        Event.created_at.desc()
    )

    result = db.execute(query)

    return list(result.scalars().all())


def get_event(
    db: Session,
    event_id: int,
) -> Event | None:
    """
    Retorna um evento pelo ID.
    """

    return db.get(Event, event_id)