from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from devtools import debug

from base_api.api.v1.runs.dependency import RunService, get_run_service
from core.schemas.run import CreateRun, UpdateRun, FilterRun
from core.config import settings


router = APIRouter(
    prefix=settings.api.v1.runs,
    tags=["Runs"],
)


@router.post("")
async def create(
    run: CreateRun,
    run_service: Annotated[
        RunService,
        Depends(get_run_service),
    ],
):
    debug(run)
    debug(run_service)
    res = await run_service.create(run)
    return res


@router.get("/{run_id}")
async def get_by_id(
    run_id: settings.db.id_type_class.get_id_type(),
    run_service: Annotated[
        RunService,
        Depends(get_run_service),
    ],
):
    res = await run_service.get_by_id(run_id)
    return res


@router.get("/")
async def get(
    run_service: Annotated[
        RunService,
        Depends(get_run_service),
    ],
    filters: Annotated[FilterRun, Depends(FilterRun)] = None,
    page: int = 1,
    size: int = 10,
):
    res = await run_service.get(
        page=page,
        size=size,
        filters=filters,
    )
    return res


@router.delete("/{run_id}")
async def delete(
    run_id: settings.db.id_type_class.get_id_type(),
    run_service: Annotated[
        RunService,
        Depends(get_run_service),
    ],
):
    res = await run_service.delete(
        obj_id=run_id,
    )
    return res


@router.patch("/{run_id}")
async def edit(
    run_id: settings.db.id_type_class.get_id_type(),
    run_update: UpdateRun,
    run_service: Annotated[
        RunService,
        Depends(get_run_service),
    ],
):
    res = await run_service.edit(
        obj_id=run_id,
        obj_in=run_update,
    )
    return res
