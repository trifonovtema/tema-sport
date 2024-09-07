from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from core.base.base_repo import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession

from core.base.types import (
    ModelType,
    CreateSchemaType,
    UpdateSchemaType,
    ReadSchemaType,
)
from core.config import settings

RepositoryType = TypeVar("RepositoryType", bound=BaseRepository)


class BaseManager(Generic[ReadSchemaType, RepositoryType]):
    def __init__(self, repository: RepositoryType):
        """
        Manager for managing entities via the repository
        :param repository: CRUD Repository
        """
        self.repository = repository

    async def get_by_id(
        self,
        obj_id: settings.db.id_type_class.get_id_type(),
    ) -> Optional[ReadSchemaType]:
        """
        Retrieve an object using the repository
        :param obj_id: Primary key of object
        :return: The object if found, otherwise None
        """
        obj = await self.repository.get_by_id(model_id=obj_id)
        return ReadSchemaType.model_validate(obj)

    async def create(self, obj_in: CreateSchemaType) -> ReadSchemaType:
        """
        Create a new object using the repository
        :param obj_in: Data for the new object
        :return: The newly created object
        """
        created_obj = await self.repository.create(obj_in)
        return ReadSchemaType.model_validate(created_obj)

    async def update(
        self,
        obj_id: settings.db.id_type_class.get_id_type(),
        obj_in: UpdateSchemaType,
    ) -> ReadSchemaType:
        """
        Update an object using the repository
        :param obj_id: Primary key of the object
        :param obj_in: Data for updating the object
        :return: The updated object
        """
        db_obj = await self.repository.get_by_id(model_id=obj_id)
        updated_obj = await self.repository.update(db_obj, obj_in)
        return ReadSchemaType.model_validate(updated_obj)

    async def delete(
        self,
        obj_id: settings.db.id_type_class.get_id_type(),
    ) -> Optional[ReadSchemaType]:
        """
        Delete an object using the repository
        :param obj_id: Primary key of the object
        :return: The deleted object, if found
        """
        deleted_obj = await self.repository.remove(model_id=obj_id)
        return ReadSchemaType.model_validate(deleted_obj)
