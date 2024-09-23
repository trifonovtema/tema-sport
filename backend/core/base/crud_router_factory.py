from devtools import debug
from typing import Type, Annotated, Callable
from fastapi import APIRouter, Depends
from core.base.base_service import BaseService
from core.base.types import CreateSchemaType, UpdateSchemaType, FilterSchemaType
from core.config import settings


def create_crud_router_factory(
    service_class: Type[BaseService],
    create_schema: Type[CreateSchemaType],
    update_schema: Type[UpdateSchemaType],
    filter_schema: Type[FilterSchemaType],
    service_dependency: Callable,
    id_type: Type[settings.db.id_type_class.get_id_type()],
    **router_kwargs
):
    router = APIRouter(**router_kwargs)

    @router.post("")
    async def create(
        obj_in: create_schema,
        service: Annotated[service_class, Depends(service_dependency)],
    ):
        debug(obj_in)
        return await service.create(obj_in)

    @router.get("/{obj_id}")
    async def get_by_id(
        obj_id: id_type,
        service: Annotated[service_class, Depends(service_dependency)],
    ):
        return await service.get_by_id(obj_id)

    @router.get("")
    async def get(
        service: Annotated[service_class, Depends(service_dependency)],
        filters: Annotated[filter_schema, Depends(filter_schema)] = None,
        page: int = 1,
        size: int = 10,
    ):
        return await service.get(page=page, size=size, filters=filters)

    @router.delete("/{obj_id}")
    async def delete(
        obj_id: id_type,
        service: Annotated[service_class, Depends(service_dependency)],
    ):
        return await service.delete(obj_id)

    @router.patch("/{obj_id}")
    async def edit(
        obj_id: id_type,
        obj_in: update_schema,
        service: Annotated[service_class, Depends(service_dependency)],
    ):
        return await service.edit(obj_id=obj_id, obj_in=obj_in)

    return router
