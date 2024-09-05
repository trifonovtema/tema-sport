from fastapi import APIRouter, Depends

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request, status

from backend.core.schemas.competition import CompetitionRead, CompetitionCreate

router = APIRouter()


@router.post(
    "/competitions",
    response_model=CompetitionRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_competition(competition: CompetitionCreate, db =):
    message = CompetitionMessage(name=name, location=location, date=date)
    await competition_service.create_competition(message)
    return {"message": "Competition created successfully"}
