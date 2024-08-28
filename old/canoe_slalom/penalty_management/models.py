from pydantic import BaseModel
from ...base.models import BaseMessage


class PenaltyMessage(BaseMessage):
    gate_number: int
    penalty_time: int
    judge_id: int
    comment: str
    attempt_number: int
