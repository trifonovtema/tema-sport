from fastapi import APIRouter, Depends
from .services import get_competition_service, CompetitionService
from .models import CompetitionMessage
from typing import Annotated

router = APIRouter()


@router.post("/competitions")
async def create_competition_endpoint(
    name: str,
    location: str,
    date: str,
    competition_service: Annotated[
        CompetitionService, Depends(get_competition_service)
    ],
):
    message = CompetitionMessage(name=name, location=location, date=date)
    await competition_service.create_competition(message)
    return {"message": "Competition created successfully"}
