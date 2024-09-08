from collections.abc import Sequence
from typing import Generic, Type, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from core.base.types import (
    CreateSchemaType,
    ModelType,
    UpdateSchemaType,
    FilterSchemaType,
)
from core.config import settings
from sqlalchemy import select


class BaseRepository(
    Generic[ModelType, CreateSchemaType, UpdateSchemaType, FilterSchemaType]
):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        """
        CRUD Repository for database operations
        :param model: SQLAlchemy model
        """
        self.model = model
        self.session = session

    async def get_by_id(
        self,
        model_id: settings.db.id_type_class.get_id_type(),
    ) -> Optional[ModelType]:
        """
        Retrieve an object by ID
        :param model_id: Primary key of object
        :return: The object if found, otherwise None
        """
        stmt = select(self.model).where(self.model.id == model_id)
        result = await self.session.scalar(stmt)
        return result

    async def get(
        self,
        skip: int,
        limit: int,
        filters: FilterSchemaType = None,
    ) -> Sequence[ModelType]:
        """
        Retrieve multiple objects with pagination
        :param skip: Number of records to skip
        :param limit: Maximum number of records to return
        :param filters: Filter parameters
        :return: List of objects
        """
        stmt = select(self.model)
        if filters:
            filter_data = filters.model_dump(exclude_unset=True)
            for field, value in filter_data.items():
                if value is not None and hasattr(self.model, field):
                    column = getattr(self.model, field)
                    stmt = stmt.where(column == value)
        stmt = stmt.order_by(self.model.created_at).offset(skip).limit(limit)
        result = await self.session.scalars(stmt)
        return result.all()

    async def create(
        self,
        obj_in: CreateSchemaType,
    ) -> ModelType:
        """
        Create a new object
        :param obj_in: Data for the new object
        :return: The newly created object
        """
        db_obj = self.model(**obj_in.model_dump())
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def edit(
        self,
        db_obj: ModelType,
        obj_in: UpdateSchemaType,
    ) -> ModelType:
        """
        Update an existing object
        :param db_obj: Current database object
        :param obj_in: Data for updating the object
        :return: The updated object
        """
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def remove(
        self,
        model_id: settings.db.id_type_class.get_id_type(),
    ) -> Optional[ModelType]:
        """
        Delete an object by ID
        :param model_id: Primary key of the object
        :return: The deleted object, if found
        """
        obj = await self.get_by_id(model_id)
        if obj:
            await self.session.delete(obj)
            await self.session.commit()
        return obj
