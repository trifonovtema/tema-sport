from pydantic import BaseModel, ConfigDict

from datetime import datetime

from core.config import settings


class BaseRace(BaseModel):
    competition_id: settings.db.id_type_class.get_id_type() | None
    name: str | None


class ReadRace(BaseRace):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateRace(BaseRace):
    competition_id: settings.db.id_type_class.get_id_type() | None = None
    name: str | None = None


class CreateRace(BaseRace):
    pass


class FilterRace(BaseRace):
    competition_id: settings.db.id_type_class.get_id_type() | None = None
    name: str | None = None
