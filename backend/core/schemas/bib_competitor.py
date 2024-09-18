from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseBibCompetitor(BaseModel):
    bib_id: Any | None
    competitor_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadBibCompetitor(BaseBibCompetitor):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateBibCompetitor(BaseBibCompetitor):
    bib_id: Any | None
    competitor_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateBibCompetitor(BaseBibCompetitor):
    pass


class FilterBibCompetitor(BaseBibCompetitor):
    bib_id: Any | None
    competitor_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
