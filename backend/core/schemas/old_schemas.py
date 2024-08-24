from typing import Any, List
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime


class KafkaMessageHeader(BaseModel):
    client_id: str | None
    trace_id: str
    type: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class KafkaMessage(BaseModel):
    header: KafkaMessageHeader
    payload: Any


class GetUsersMessage(BaseModel):
    skip: int
    limit: int
    user_id: UUID | None = None

    class Config:
        from_attributes = True
        json_encoders = {UUID: lambda v: str(v)}


class AddUser(BaseModel):
    name: str | None = None


class User(AddUser):
    id: UUID | None = None

    class Config:
        from_attributes = True
        json_encoders = {UUID: lambda v: str(v)}


class ProcessUser(BaseModel):
    id: UUID | None = None
    user: User | None = None

    class Config:
        from_attributes = True
        json_encoders = {UUID: lambda v: str(v)}


class GetUsersResult(BaseModel):
    users: List[User]
    next_exists: bool
    page: int
    page_size: int


class DeletedUser(BaseModel):
    id: UUID | None = None

    class Config:
        from_attributes = True
        json_encoders = {UUID: lambda v: str(v)}


class APIResponse(BaseModel):
    trace_id: str
    status: str
    message: str


class ConfirmationMessage(BaseModel):
    status: str
    payload: Any


class UserKafkaMessage(KafkaMessage, User):
    pass
