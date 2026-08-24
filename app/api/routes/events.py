"""
Endpoints relacionados aos eventos.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from repositories.event_repository import (
    get_event,
    get_events,
)
from schemas.event import (
    EventCreate,
    EventQueuedResponse,
    EventResponse,
)
from services.event_service import create_and_queue_event


router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@router.post(
    "/",
    response_model=EventQueuedResponse,
    status_code=202,
)
def create_new_event(
    event_data: EventCreate,
    db: Session = Depends(get_db),
):
    """
    Cria um evento e coloca seu processamento
    em uma fila assíncrona.
    """

    event, task_id = create_and_queue_event(
        db=db,
        event_data=event_data,
    )

    return {
        "event_id": event.id,
        "task_id": task_id,
        "status": "queued",
    }


@router.get(
    "/",
    response_model=list[EventResponse],
)
def list_events(
    db: Session = Depends(get_db),
):
    """
    Retorna todos os eventos.
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
    Retorna um evento específico.
    """

    event = get_event(
        db=db,
        event_id=event_id,
    )

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found",
        )

    return event