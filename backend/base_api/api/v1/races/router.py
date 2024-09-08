from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from devtools import debug

from base_api.api.v1.races.dependency import RaceService, get_race_service
from core.schemas.race import CreateRace, UpdateRace, FilterRace
from core.config import settings


router = APIRouter(
    prefix=settings.api.v1.races,
    tags=["Races"],
)


@router.post("")
async def create_race(
    race: CreateRace,
    race_service: Annotated[
        RaceService,
        Depends(get_race_service),
    ],
):
    debug(race)
    res = await race_service.create(race)
    return res


@router.get("/{race_id}")
async def get_race_by_id(
    race_id: settings.db.id_type_class.get_id_type(),
    race_service: Annotated[
        RaceService,
        Depends(get_race_service),
    ],
):
    res = await race_service.get_by_id(race_id)
    return res


@router.get("/")
async def get_races(
    race_service: Annotated[
        RaceService,
        Depends(get_race_service),
    ],
    filters: Annotated[FilterRace, Depends(FilterRace)] = None,
    page: int = 1,
    size: int = 10,
):
    res = await race_service.get(
        page=page,
        size=size,
        filters=filters,
    )
    return res


@router.delete("/{race_id}")
async def delete_races(
    race_id: settings.db.id_type_class.get_id_type(),
    race_service: Annotated[
        RaceService,
        Depends(get_race_service),
    ],
):
    res = await race_service.delete(
        obj_id=race_id,
    )
    return res


@router.patch("/{race_id}")
async def edit_races(
    race_id: settings.db.id_type_class.get_id_type(),
    race_update: UpdateRace,
    race_service: Annotated[
        RaceService,
        Depends(get_race_service),
    ],
):
    res = await race_service.edit(
        obj_id=race_id,
        obj_in=race_update,
    )
    return res
