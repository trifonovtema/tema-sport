from pydantic import BaseModel


class BaseMessage(BaseModel):
    participant_id: int
    race_id: int
