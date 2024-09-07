from typing import Any
from pydantic import BaseModel, Field
from datetime import datetime
from constants import KafkaTopic, MessageType


class KafkaMessageHeader(BaseModel):
    client_id: str | None
    trace_id: str
    message_type: MessageType
    response_topic: KafkaTopic
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KafkaMessage(BaseModel):
    header: KafkaMessageHeader
    payload: Any


class ResponseMessage(BaseModel):
    status: str
    payload: Any
