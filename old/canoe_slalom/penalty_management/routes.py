from fastapi import APIRouter
from .services import PenaltyService
from .models import PenaltyMessage

router = APIRouter()
penalty_service = PenaltyService()


@router.post("/penalties")
async def add_penalty_endpoint(
    participant_id: int,
    gate_number: int,
    penalty_time: int,
    judge_id: int,
    comment: str,
    attempt_number: int,
    race_id: int,
):
    message = PenaltyMessage(
        participant_id=participant_id,
        gate_number=gate_number,
        penalty_time=penalty_time,
        judge_id=judge_id,
        comment=comment,
        attempt_number=attempt_number,
        race_id=race_id,
    )
    await penalty_service.add_penalty(message)
    return {"message": "Penalty added successfully"}
