from pydantic import BaseModel
from uuid import UUID


class CompetitionCreate(BaseModel):
    name: str


class CompetitionRead(CompetitionCreate):
    id: UUID


class CompetitionUpdate(CompetitionRead):
    pass
