"""
Endpoints relacionados aos eventos.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.database import get_db
from repositories.event_repository import (
    get_event,
    get_events,
)
from schemas.event import (
    EventCreate,
    EventResponse,
)
from services.event_service import (
    create_and_publish_event,
)


router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@router.post(
    "/",
    response_model=dict,
    status_code=status.HTTP_202_ACCEPTED,
)
def create_new_event(
    event_data: EventCreate,
    db: Session = Depends(get_db),
):
    """
    Cria um evento e publica no Kafka.
    """

    event, metadata = create_and_publish_event(
        db=db,
        event_data=event_data,
    )

    return {
        "event_id": event.id,
        "status": "published",
        "kafka": {
            "topic": metadata["topic"],
            "partition": metadata["partition"],
            "offset": metadata["offset"],
        },
    }


@router.get(
    "/",
    response_model=list[EventResponse],
)
def list_events(
    db: Session = Depends(get_db),
):
    """
    Lista os eventos.
    """

    return get_events(db)


@router.get(
    "/{event_id}",
    response_model=EventResponse,
)
def get_event_by_id(
    event_id: int,
    db: Session = Depends(get_db),
):
    """
    Busca um evento específico.
    """

    return get_event(
        db=db,
        event_id=event_id,
    )