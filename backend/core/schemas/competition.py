from typing import Any
from pydantic import BaseModel, Field
from datetime import datetime
from backend.constants import KafkaTopic, MessageType
from backend.core.types.event import EventType
from uuid import UUID


class CompetitionCreate(BaseModel):
    name: str


class CompetitionRead(CompetitionCreate):
    id: UUID


class CompetitionUpdate(CompetitionRead):
    pass
