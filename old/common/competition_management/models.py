from pydantic import BaseModel


class CompetitionMessage(BaseModel):
    name: str
    location: str
    date: str
