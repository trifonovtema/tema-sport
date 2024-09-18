from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseBibPool(BaseModel):
    bib_number: int
    is_exists: bool
    competition_id: settings.db.id_type_class.get_id_type()


class ReadBibPool(BaseBibPool):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateBibPool(BaseBibPool):
    bib_number: int | None = None
    is_exists: bool | None = None
    competition_id: settings.db.id_type_class.get_id_type() | None = None


class CreateBibPool(BaseBibPool):
    pass


class FilterBibPool(BaseBibPool):
    bib_number: int | None = None
    is_exists: bool | None = None
    competition_id: settings.db.id_type_class.get_id_type() | None = None
