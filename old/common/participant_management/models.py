from pydantic import BaseModel
from ...base.models import BaseMessage


class ParticipantMessage(BaseMessage):
    name: str
    age: int
    gender: str
