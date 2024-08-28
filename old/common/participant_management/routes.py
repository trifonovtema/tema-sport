from fastapi import APIRouter
from .services import ParticipantService
from .models import ParticipantMessage

router = APIRouter()
participant_service = ParticipantService()


@router.post("/participants")
async def add_participant_endpoint(name: str, age: int, gender: str, race_id: int):
    message = ParticipantMessage(name=name, age=age, gender=gender, race_id=race_id)
    await participant_service.add_participant(message)
    return {"message": "Participant added successfully"}
