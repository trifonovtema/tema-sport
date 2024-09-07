from fastapi import Depends
from core.base.control_classes.base_manager import BaseManager
from core.base.control_classes.base_repo import BaseRepository
from core.base.control_classes.base_service import BaseService
from core.models import db_helper, Run
from typing import Annotated
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from core.schemas.run import CreateRun, UpdateRun, ReadRun, FilterRun


class RunRepository(BaseRepository[Run, CreateRun, UpdateRun, FilterRun]):
    pass


class RunManager(BaseManager[RunRepository, ReadRun, FilterRun]):
    pass


class RunService(BaseService[RunManager, ReadRun, FilterRun]):
    pass


async def get_async_session() -> AsyncSession:
    async with db_helper.session_factory() as session:
        try:
            yield session
        finally:
            await session.close()


async def get_run_repo(
    session: Annotated[AsyncSession, Depends(get_async_session)],
) -> RunRepository:
    return RunRepository(Run, session)


async def get_run_manager(
    repo: Annotated[RunRepository, Depends(get_run_repo)],
) -> RunManager:
    return RunManager(repo, ReadRun)


async def get_run_service(
    manager: Annotated[RunManager, Depends(get_run_manager)],
) -> RunService:
    return RunService(manager)
