from typing import Type, TypeVar, Callable
from sqlalchemy.ext.asyncio import AsyncSession
from core.base.base_repo import BaseRepository
from core.base.base_manager import BaseManager
from core.base.base_service import BaseService
from core.base.types import (
    ModelType,
    CreateSchemaType,
    UpdateSchemaType,
    ReadSchemaType,
    FilterSchemaType,
)


# class Factory:
#     @staticmethod
#     def create_repository(
#         model: Type[ModelType],
#         create_schema: Type[CreateSchemaType],
#         update_schema: Type[UpdateSchemaType],
#     ) -> Callable[
#         [AsyncSession],
#         BaseRepository[ModelType, CreateSchemaType, UpdateSchemaType, FilterSchemaType],
#     ]:
#         def get_repo(
#             session: AsyncSession,
#         ) -> BaseRepository[
#             ModelType,
#             CreateSchemaType,
#             UpdateSchemaType,
#             FilterSchemaType,
#             FilterSchemaType,
#         ]:
#             return BaseRepository(model, session)
#
#         return get_repo
#
#     @staticmethod
#     def create_manager(
#         read_schema: Type[ReadSchemaType],
#     ) -> Callable[
#         [BaseRepository], BaseManager[ReadSchemaType, BaseRepository, FilterSchemaType]
#     ]:
#         def get_manager(
#             repository: BaseRepository,
#         ) -> BaseManager[ReadSchemaType, BaseRepository, FilterSchemaType]:
#             return BaseManager(repository)
#
#         return get_manager
#
#     @staticmethod
#     def create_service() -> Callable[
#         [BaseManager],
#         BaseService,
#     ]:
#         def get_service(manager: BaseManager) -> BaseService:
#             return BaseService(manager)
#
#         return get_service
