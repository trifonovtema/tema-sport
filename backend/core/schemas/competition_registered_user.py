from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseCompetitionRegisteredUser(BaseModel):
    user_id: Any | None
    competition_id: Any | None
    type: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadCompetitionRegisteredUser(BaseCompetitionRegisteredUser):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateCompetitionRegisteredUser(BaseCompetitionRegisteredUser):
    user_id: Any | None
    competition_id: Any | None
    type: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateCompetitionRegisteredUser(BaseCompetitionRegisteredUser):
    pass


class FilterCompetitionRegisteredUser(BaseCompetitionRegisteredUser):
    user_id: Any | None
    competition_id: Any | None
    type: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
