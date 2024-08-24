from uuid import UUID

from fastapi import APIRouter

from backend.core.schemas.run import Competition
from backend.core.schemas.common import APIResponse

from .services import KafkaCompetitionsService

router = APIRouter(prefix="/competitions", tags=["Competitions"])
kafka_service = KafkaCompetitionsService()


@router.post("/", response_model=APIResponse)
async def add(competition: Competition):
    print(f"{competition=}")
    res = await kafka_service.add(competition=competition, client_id="1")
    return res


@router.post("/{competition_id}", response_model=APIResponse)
async def update(competition: Competition, competition_id: UUID):
    print(f"{competition=}")
    res = await kafka_service.update(
        competition=competition, competition_id=competition_id, client_id="1"
    )
    return res


@router.delete("/{competition_id}", response_model=APIResponse)
async def delete(competition_id: UUID):
    res = await kafka_service.delete(competition_id=competition_id, client_id="1")
    return res


@router.get("/{competition_id}", response_model=APIResponse)
async def get_by_id(competition_id: UUID):
    res = await kafka_service.get(competition_id=competition_id, client_id="1")
    return res


@router.get("/", response_model=APIResponse)
async def get(page: int = 1, page_size: int = 10):
    skip = (page - 1) * page_size
    limit = page_size
    res = await kafka_service.get(client_id="1", skip=skip, limit=limit)
    return res
