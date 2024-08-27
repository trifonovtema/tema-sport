import uuid
from abc import ABC

from sqlalchemy import Integer as sqlalchemy_integer, UUID as sqlalchemy_uuid


class IdType(ABC):
    id_type = None  # int
    id_type_sqlalchemy = None  # Integer


class IdTypeInt(IdType):
    id_type = int
    id_type_sqlalchemy = sqlalchemy_integer


class IdTypeUuid(IdType):
    id_type = uuid.UUID
    id_type_sqlalchemy = sqlalchemy_uuid
