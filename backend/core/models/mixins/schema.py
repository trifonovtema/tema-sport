from sqlalchemy.orm import declared_attr
from core.config import settings


class SchemaNameMixin:
    @declared_attr
    def __table_args__(cls):
        return {"schema": settings.db.SCHEMA}
