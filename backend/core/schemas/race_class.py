from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseRaceClass(BaseModel):
    name: int | None
    athletes_qualified_count: int | None
    athletes_qualified_percentage: int | None
    race_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadRaceClass(BaseRaceClass):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateRaceClass(BaseRaceClass):
    name: int | None
    athletes_qualified_count: int | None
    athletes_qualified_percentage: int | None
    race_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateRaceClass(BaseRaceClass):
    pass


class FilterRaceClass(BaseRaceClass):
    name: int | None
    athletes_qualified_count: int | None
    athletes_qualified_percentage: int | None
    race_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
