from pydantic import BaseModel
from ...base.models import BaseMessage


class StartTimeMessage(BaseMessage):
    start_time: int


class FinishTimeMessage(BaseMessage):
    finish_time: int


class PenaltyMessage(BaseMessage):
    gate_number: int
    penalty_time: int
    judge_id: int
    comment: str
    attempt_number: int


class SplitTimeMessage(BaseMessage):
    split_time: int
    split_number: int
    gate_number: int
