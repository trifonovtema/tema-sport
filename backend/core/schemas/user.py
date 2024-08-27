from fastapi_users import schemas

from backend.settings import get_settings


class UserRead(schemas.BaseUser[get_settings().db.id_type.id_type]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
