from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseBib(BaseModel):
    bib_number: int | None


class ReadBib(BaseBib):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateBib(BaseBib):
    bib_number: int | None


class CreateBib(BaseBib):
    pass


class FilterBib(BaseBib):
    bib_number: int | None
