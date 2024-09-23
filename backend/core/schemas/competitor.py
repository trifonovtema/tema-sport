from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseCompetitor(BaseModel):
    race_class_id: settings.db.id_type_class.get_id_type() | None


class ReadCompetitor(BaseCompetitor):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateCompetitor(BaseCompetitor):
    race_class_id: settings.db.id_type_class.get_id_type() | None


class CreateCompetitor(BaseCompetitor):
    pass


class FilterCompetitor(BaseCompetitor):
    race_class_id: settings.db.id_type_class.get_id_type() | None
