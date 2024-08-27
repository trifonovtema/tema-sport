import uuid
from abc import ABC
from fastapi_users import UUIDIDMixin, IntegerIDMixin
from sqlalchemy import Integer as SqlalchemyInteger, UUID as SQLALCHEMY_UUID


class IdType(ABC):
    id_type = None  # int
    id_type_sqlalchemy = None  # Integer
    id_mixin = None


class IdTypeInt(IdType):
    id_type = int
    id_type_sqlalchemy = SqlalchemyInteger
    id_mixin = IntegerIDMixin


class IdTypeUuid(IdType):
    id_type = uuid.UUID
    id_type_sqlalchemy = SQLALCHEMY_UUID
    id_mixin = UUIDIDMixin
