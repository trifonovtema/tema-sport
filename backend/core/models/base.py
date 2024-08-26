from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr

from backend.settings import get_settings
from backend.utils.snake_converter import camel_case_to_snake_case

settings = get_settings()


class Base(DeclarativeBase):
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
