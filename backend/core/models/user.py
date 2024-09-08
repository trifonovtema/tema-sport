from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from .base import Base
from core.config import settings


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(
    Base,
    SQLAlchemyBaseUserTable[settings.db.id_type_class.get_id_type()],
):

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
