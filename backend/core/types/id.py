import uuid
from abc import ABC, abstractmethod
from fastapi_users import UUIDIDMixin, IntegerIDMixin
from sqlalchemy import Integer as SqlalchemyInteger, UUID as SQLALCHEMY_UUID


class IdType(ABC):
    """Абстрактный класс для типов ID."""

    @abstractmethod
    def get_id_type(self):
        pass

    @abstractmethod
    def get_sqlalchemy_type(self):
        pass

    @abstractmethod
    def get_id_mixin(self):
        pass


class IdTypeInt(IdType):
    """Класс для работы с int ID."""

    def get_id_type(self):
        return int

    def get_sqlalchemy_type(self):
        return SqlalchemyInteger

    def get_id_mixin(self):
        return IntegerIDMixin


class IdTypeUuid(IdType):
    """Класс для работы с UUID ID."""

    def get_id_type(self):
        return uuid.UUID

    def get_sqlalchemy_type(self):
        return SQLALCHEMY_UUID

    def get_id_mixin(self):
        return UUIDIDMixin
