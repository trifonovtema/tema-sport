from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseCompetitionOwner(BaseModel):
    competition_id: Any | None
    user_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadCompetitionOwner(BaseCompetitionOwner):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateCompetitionOwner(BaseCompetitionOwner):
    competition_id: Any | None
    user_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateCompetitionOwner(BaseCompetitionOwner):
    pass


class FilterCompetitionOwner(BaseCompetitionOwner):
    competition_id: Any | None
    user_id: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
