from typing import Generic, TypeVar, Optional, Type
from core.base.base_repo import BaseRepository
from core.base.types import (
    CreateSchemaType,
    UpdateSchemaType,
    ReadSchemaType,
    FilterSchemaType,
)
from core.config import settings

RepositoryType = TypeVar("RepositoryType", bound=BaseRepository)


class BaseManager(Generic[RepositoryType, ReadSchemaType, FilterSchemaType]):
    def __init__(
        self,
        repository: RepositoryType,
        read_schema: Type[ReadSchemaType],
    ):
        """
        Manager for managing entities via the repository
        :param repository: CRUD Repository
        """
        self.repository = repository
        self.read_schema = read_schema

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
        return self.read_schema.model_validate(obj)

    async def get(
        self,
        filters: FilterSchemaType = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[ReadSchemaType]:
        """
        Retrieve an object using the repository
        :skip: int = 0,
        :limit: int = 100,
        :return: The object if found, otherwise None
        """
        objects = await self.repository.get(
            limit=limit,
            skip=skip,
            filters=filters,
        )
        res: list[ReadSchemaType] = []
        for obj in objects:
            res.append(self.read_schema.model_validate(obj))
        return res

    async def create(self, obj_in: CreateSchemaType) -> ReadSchemaType:
        """
        Create a new object using the repository
        :param obj_in: Data for the new object
        :return: The newly created object
        """
        created_obj = await self.repository.create(obj_in)
        return self.read_schema.model_validate(created_obj)

    async def edit(
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
        if db_obj:
            updated_obj = await self.repository.edit(db_obj, obj_in)
            return self.read_schema.model_validate(updated_obj)
        else:
            # TODO process situation where obj not found
            pass

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
        return self.read_schema.model_validate(deleted_obj)
