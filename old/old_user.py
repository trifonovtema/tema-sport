from typing import List
from uuid import UUID
from pydantic import BaseModel


class GetMessage(BaseModel):
    skip: int
    limit: int
    id: UUID | None = None

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
