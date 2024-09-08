from pydantic import BaseModel
from backend.core.types.event import EventType
from uuid import UUID


class EventCreate(BaseModel):
    name: str
    type: EventType


class EventRead(EventCreate):
    id: UUID


class EventUpdate(EventRead):
    pass
