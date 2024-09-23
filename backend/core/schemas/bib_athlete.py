from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseBibAthlete(BaseModel):
    athlete_id: settings.db.id_type_class.get_id_type() | None
    bib_id: settings.db.id_type_class.get_id_type() | None


class ReadBibAthlete(BaseBibAthlete):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateBibAthlete(BaseBibAthlete):
    athlete_id: settings.db.id_type_class.get_id_type() | None
    bib_id: settings.db.id_type_class.get_id_type() | None


class CreateBibAthlete(BaseBibAthlete):
    pass


class FilterBibAthlete(BaseBibAthlete):
    athlete_id: settings.db.id_type_class.get_id_type() | None
    bib_id: settings.db.id_type_class.get_id_type() | None
