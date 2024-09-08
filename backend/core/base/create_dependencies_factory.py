from typing import Annotated, Type
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.types import ModelType
from dependencies.db.async_session import get_async_session


def create_dependency_factory(
    repo_class: Type[BaseRepository],
    manager_class: Type[BaseManager],
    service_class: Type[BaseService],
    model: Type[ModelType],
    create_schema,
    update_schema,
    read_schema,
    filter_schema,
):
    async def get_repo(
        session: Annotated[AsyncSession, Depends(get_async_session)],
    ) -> repo_class:
        return repo_class(model, session)

    async def get_manager(
        repo: Annotated[repo_class, Depends(get_repo)],
    ) -> manager_class:
        return manager_class(repo, read_schema)

    async def get_service(
        manager: Annotated[manager_class, Depends(get_manager)],
    ) -> service_class:
        return service_class(manager)

    return get_repo, get_manager, get_service
