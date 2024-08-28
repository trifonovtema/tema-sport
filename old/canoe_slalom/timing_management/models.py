from pydantic import BaseModel
from ...base.models import BaseMessage


class StartTimeMessage(BaseMessage):
    start_time: int


class FinishTimeMessage(BaseMessage):
    finish_time: int


class SplitTimeMessage(BaseMessage):
    split_time: int
    split_number: int
    gate_number: int
