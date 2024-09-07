from fastapi_users import schemas

from core.config import settings


class UserRead(schemas.BaseUser[settings.db.id_type_class.get_id_type()]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
