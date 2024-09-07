from uuid import UUID

from pydantic import BaseModel
from pydantic import AliasPath, BaseModel, ConfigDict, Field

from datetime import datetime

from core.config import settings


class BaseRun(BaseModel):
    user_id: settings.db.id_type_class.get_id_type() | None
    race_id: settings.db.id_type_class.get_id_type() | None
    name: str | None
    # scheduled_time: datetime | None


class ReadRun(BaseRun):
    id: settings.db.id_type_class.get_id_type()
    # created_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateRun(BaseRun):
    pass


class CreateRun(BaseRun):
    pass
