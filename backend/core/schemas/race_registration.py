from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseRaceRegistration(BaseModel):
    race_id: Any | None
    competitor_id: Any | None
    race_class_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadRaceRegistration(BaseRaceRegistration):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateRaceRegistration(BaseRaceRegistration):
    race_id: Any | None
    competitor_id: Any | None
    race_class_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateRaceRegistration(BaseRaceRegistration):
    pass


class FilterRaceRegistration(BaseRaceRegistration):
    race_id: Any | None
    competitor_id: Any | None
    race_class_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
