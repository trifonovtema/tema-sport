from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseAthlete(BaseModel):
    competition_registered_user_id: settings.db.id_type_class.get_id_type() | None
    race_id: settings.db.id_type_class.get_id_type() | None


class ReadAthlete(BaseAthlete):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateAthlete(BaseAthlete):
    competition_registered_user_id: settings.db.id_type_class.get_id_type() | None
    race_id: settings.db.id_type_class.get_id_type() | None


class CreateAthlete(BaseAthlete):
    pass


class FilterAthlete(BaseAthlete):
    competition_registered_user_id: settings.db.id_type_class.get_id_type() | None
    race_id: settings.db.id_type_class.get_id_type() | None
