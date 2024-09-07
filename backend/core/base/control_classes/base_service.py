from typing import Generic, TypeVar, Optional
from core.base.control_classes.base_manager import BaseManager
from core.base.types import (
    ReadSchemaType,
    CreateSchemaType,
    UpdateSchemaType,
    FilterSchemaType,
)
from core.config import settings

# Type variables for the model and manager
ManagerType = TypeVar("ManagerType", bound=BaseManager)


class BaseService(Generic[ManagerType, ReadSchemaType, FilterSchemaType]):
    def __init__(self, manager: ManagerType):
        """
        Service for handling business logic
        :param manager: Manager for interacting with entities
        """
        self.manager = manager

    async def get_by_id(
        self,
        obj_id: settings.db.id_type_class.get_id_type(),
    ) -> Optional[ReadSchemaType]:
        """
        Retrieve an object using the repository
        :param obj_id: Primary key of object
        :return: The object if found, otherwise None
        """
        return await self.manager.get_by_id(obj_id)

    async def get(
        self,
        filters: FilterSchemaType = None,
        page: int = 1,
        size: int = 100,
    ) -> list[ReadSchemaType]:
        """
        Retrieve an object using the repository
        :return: The object if found, otherwise None
        """
        skip = (page - 1) * size
        limit = size
        return await self.manager.get(filters=filters, skip=skip, limit=limit)

    async def create(
        self,
        obj_in: CreateSchemaType,
    ) -> ReadSchemaType:
        """
        Create a new object using the repository
        :param obj_in: Data for the new object
        :return: The newly created object
        """
        return await self.manager.create(obj_in)

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
        return await self.manager.update(
            obj_id=obj_id,
            obj_in=obj_in,
        )

    async def delete(
        self,
        obj_id: settings.db.id_type_class.get_id_type(),
    ) -> Optional[ReadSchemaType]:
        """
        Delete an object using the repository
        :param obj_id: Primary key of the object
        :return: The deleted object, if found
        """
        return await self.manager.delete(obj_id=obj_id)
