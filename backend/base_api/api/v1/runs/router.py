from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from devtools import debug

from base_api.api.v1.runs.dependency import RunService, get_run_service
from core.schemas.run import CreateRun
from core.schemas.user import UserRead, UserUpdate
from base_api.api.v1.users.fastapi_users_router import fastapi_users
from core.config import settings


router = APIRouter(
    prefix=settings.api.v1.runs,
    tags=["Runs"],
)


@router.post("")
async def create_run(
    run: CreateRun,
    run_service: Annotated[
        RunService,
        Depends(get_run_service),
    ],
):
    debug(run)
    res = await run_service.create(run)
    return res
