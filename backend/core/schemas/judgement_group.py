from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseJudgementGroup(BaseModel):
    competition_registered_user_id: settings.db.id_type_class.get_id_type() | None


class ReadJudgementGroup(BaseJudgementGroup):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateJudgementGroup(BaseJudgementGroup):
    competition_registered_user_id: settings.db.id_type_class.get_id_type() | None = (
        None
    )


class CreateJudgementGroup(BaseJudgementGroup):
    pass


class FilterJudgementGroup(BaseJudgementGroup):
    competition_registered_user_id: settings.db.id_type_class.get_id_type() | None = (
        None
    )
