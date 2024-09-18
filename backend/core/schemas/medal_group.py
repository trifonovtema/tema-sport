from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseMedalGroup(BaseModel):
    group_name: Any | None
    group_type: Any | None
    competition_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadMedalGroup(BaseMedalGroup):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateMedalGroup(BaseMedalGroup):
    group_name: Any | None
    group_type: Any | None
    competition_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateMedalGroup(BaseMedalGroup):
    pass


class FilterMedalGroup(BaseMedalGroup):
    group_name: Any | None
    group_type: Any | None
    competition_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
