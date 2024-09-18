from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseUserProfile(BaseModel):
    user_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadUserProfile(BaseUserProfile):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateUserProfile(BaseUserProfile):
    user_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateUserProfile(BaseUserProfile):
    pass


class FilterUserProfile(BaseUserProfile):
    user_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
