from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseCompetitorMedalGroup(BaseModel):
    competitor_id: Any | None
    medal_group_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadCompetitorMedalGroup(BaseCompetitorMedalGroup):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateCompetitorMedalGroup(BaseCompetitorMedalGroup):
    competitor_id: Any | None
    medal_group_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateCompetitorMedalGroup(BaseCompetitorMedalGroup):
    pass


class FilterCompetitorMedalGroup(BaseCompetitorMedalGroup):
    competitor_id: Any | None
    medal_group_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
