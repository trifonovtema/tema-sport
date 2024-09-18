from core.models.mixins.created_at import CreatedAtMixin
from core.models.mixins.schema import SchemaNameMixin
from core.models.mixins.table import TableNameMixin
from core.models.mixins.updated_at import UpdatedAtMixin
from core.models.mixins.id_pk import IdPkMixin
from sqlalchemy import MetaData
from sqlalchemy.orm import declared_attr

from core.config import settings
from utils.snake_converter import camel_case_to_snake_case
from sqlalchemy.orm import DeclarativeBase


class Base(
    IdPkMixin,
    CreatedAtMixin,
    UpdatedAtMixin,
    SchemaNameMixin,
    TableNameMixin,
    DeclarativeBase,
):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )
