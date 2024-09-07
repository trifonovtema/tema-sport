from fastapi import Depends
from core.base.control_classes.base_manager import BaseManager
from core.base.control_classes.base_repo import BaseRepository
from core.base.control_classes.base_service import BaseService
from core.models import db_helper, Race
from typing import Annotated
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from core.schemas.race import CreateRace, UpdateRace, ReadRace, FilterRace


class RaceRepository(BaseRepository[Race, CreateRace, UpdateRace, FilterRace]):
    pass


class RaceManager(BaseManager[RaceRepository, ReadRace, FilterRace]):
    pass


class RaceService(BaseService[RaceManager, ReadRace, FilterRace]):
    pass


async def get_async_session() -> AsyncSession:
    async with db_helper.session_factory() as session:
        try:
            yield session
        finally:
            await session.close()


async def get_race_repo(
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> RaceRepository:
    return RaceRepository(Race, session)


async def get_race_manager(
    repo: Annotated[RaceRepository, Depends(get_race_repo)],
) -> RaceManager:
    return RaceManager(repo, ReadRace)


async def get_race_service(
    manager: Annotated[RaceManager, Depends(get_race_manager)],
) -> RaceService:
    return RaceService(manager)
