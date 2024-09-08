from uuid import UUID

from pydantic import BaseModel
from backend.constants import Penalty, CourseSegmentType

from datetime import datetime


class Competition(BaseModel):
    id: UUID | None = None
    name: str | None = None


class ProcessCompetition(BaseModel):
    id: UUID | None = None
    competition: Competition | None = None

    class Config:
        from_attributes = True
        json_encoders = {UUID: lambda v: str(v)}


class Race(BaseModel):
    id: UUID | None = None
    competition_id: UUID
    name: str


class Run(BaseModel):
    user_id: UUID
    race_id: UUID
    name: str
    scheduled_time: datetime


class GatePenalty(BaseModel):
    penalty: Penalty
    note: str


class CourseSegment(BaseModel):
    id: UUID
    number: int
    run_id: UUID
    type: CourseSegmentType
    penalty: GatePenalty | None = None
    split_time: datetime | None = None
