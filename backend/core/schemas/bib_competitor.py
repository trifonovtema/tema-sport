from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseBibCompetitor(BaseModel):
    bib_id: settings.db.id_type_class.get_id_type() | None
    competitor_id: settings.db.id_type_class.get_id_type() | None


class ReadBibCompetitor(BaseBibCompetitor):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateBibCompetitor(BaseBibCompetitor):
    bib_id: settings.db.id_type_class.get_id_type() | None
    competitor_id: settings.db.id_type_class.get_id_type() | None


class CreateBibCompetitor(BaseBibCompetitor):
    pass


class FilterBibCompetitor(BaseBibCompetitor):
    bib_id: settings.db.id_type_class.get_id_type() | None
    competitor_id: settings.db.id_type_class.get_id_type() | None
