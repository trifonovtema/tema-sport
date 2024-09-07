from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr

from core.config import settings
from core.models.mixins.created_at import CreatedAtMixin
from core.models.mixins.updated_at import UpdatedAtMixin
from utils.snake_converter import camel_case_to_snake_case
from core.models.mixins.id_pk import IdPkMixin


class Base(IdPkMixin, CreatedAtMixin, UpdatedAtMixin, DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"

    @declared_attr
    def __table_args__(cls):
        return {"schema": settings.db.SCHEMA}
