from uuid import UUID

from fastapi import APIRouter
from backend.core.schemas.old_user import User
from backend.core.schemas.common import APIResponse

from .services import KafkaUsersService

router = APIRouter(prefix="/users", tags=["Users"])
kafka_service = KafkaUsersService()


@router.post("/", response_model=APIResponse)
async def add(user: User):
    print(f"{user=}")
    res = await kafka_service.add(user=user, client_id="1")
    return res


@router.post("/{user_id}", response_model=APIResponse)
async def update(user: User, user_id: UUID):
    print(f"{user=}")
    res = await kafka_service.update(user=user, user_id=user_id, client_id="1")
    return res


@router.delete("/{user_id}", response_model=APIResponse)
async def delete_user(user_id: UUID):
    res = await kafka_service.delete(user_id=user_id, client_id="1")
    return res


@router.get("/{user_id}", response_model=APIResponse)
async def get_by_id(user_id: UUID):
    res = await kafka_service.get(user_id=user_id, client_id="1")
    return res


@router.get("/", response_model=APIResponse)
async def get(page: int = 1, page_size: int = 10):
    """
    Read current user parameters.
    """
    skip = (page - 1) * page_size
    limit = page_size
    res = await kafka_service.get(client_id="1", skip=skip, limit=limit)
    return res
