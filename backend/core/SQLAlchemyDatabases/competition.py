from typing import Optional, Dict, Any
from sqlalchemy import select

from backend.core.SQLAlchemyDatabases.base import BaseDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.models.competition import Competition
from core.config import get_settings
from sqlalchemy.sql import Select


class SQLAlchemyCompetitionDatabase(BaseDatabase):
    """
    Database adapter for SQLAlchemy.

    :param session: SQLAlchemy session instance.
    :param user_table: SQLAlchemy user model.
    :param oauth_account_table: Optional SQLAlchemy OAuth accounts model.
    """

    session: AsyncSession
    table: Competition

    def __init__(
        self,
        session: AsyncSession,
        table: Competition,
    ):
        self.session = session
        self.table = table

    async def get_by_id(
        self, competition_id: get_settings().db.id_type_class.get_id_type()
    ) -> Optional[Competition]:
        statement = select(self.table).where(self.table.id == competition_id)
        return await self._get_competition(statement)

    async def create(self, create_dict: Dict[str, Any]) -> Competition:
        user = self.table(**create_dict)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def update(
        self, competition: Competition, update_dict: Dict[str, Any]
    ) -> Competition:
        for key, value in update_dict.items():
            setattr(competition, key, value)
        self.session.add(competition)
        await self.session.commit()
        await self.session.refresh(competition)
        return competition

    async def delete(self, competition: Competition) -> None:
        await self.session.delete(competition)
        await self.session.commit()

    async def _get_competition(self, statement: Select) -> Optional[Competition]:
        results = await self.session.execute(statement)
        return results.unique().scalar_one_or_none()
