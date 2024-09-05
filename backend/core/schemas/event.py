from typing import Any
from pydantic import BaseModel, Field
from datetime import datetime
from backend.constants import KafkaTopic, MessageType
from backend.core.types.event import EventType
from uuid import UUID


class EventCreate(BaseModel):
    name: str
    type: EventType


class EventRead(EventCreate):
    id: UUID


class EventUpdate(EventRead):
    pass
