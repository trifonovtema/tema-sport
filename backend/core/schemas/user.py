from fastapi_users import schemas
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class UserRead(schemas.BaseUser[settings.db.id_type_class.get_id_type()]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class BaseUser(BaseModel):
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
    email: str | None
    hashed_password: str | None
    is_active: bool | None
    is_superuser: bool | None
    is_verified: bool | None


class ReadUser(BaseUser):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateUser(BaseUser):
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
    email: str | None
    hashed_password: str | None
    is_active: bool | None
    is_superuser: bool | None
    is_verified: bool | None


class CreateUser(BaseUser):
    pass


class FilterUser(BaseUser):
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
    email: str | None
    hashed_password: str | None
    is_active: bool | None
    is_superuser: bool | None
    is_verified: bool | None
