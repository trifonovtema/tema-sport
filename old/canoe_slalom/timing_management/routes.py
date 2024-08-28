from fastapi import APIRouter
from .services import TimingService
from .models import StartTimeMessage, FinishTimeMessage, SplitTimeMessage

router = APIRouter()
timing_service = TimingService()


@router.post("/times/start")
async def record_start_time_endpoint(
    participant_id: int, start_time: int, race_id: int
):
    message = StartTimeMessage(
        participant_id=participant_id, start_time=start_time, race_id=race_id
    )
    await timing_service.record_start_time(message)
    return {"message": "Start time recorded successfully"}


@router.post("/times/finish")
async def record_finish_time_endpoint(
    participant_id: int, finish_time: int, race_id: int
):
    message = FinishTimeMessage(
        participant_id=participant_id, finish_time=finish_time, race_id=race_id
    )
    await timing_service.record_finish_time(message)
    return {"message": "Finish time recorded successfully"}


@router.post("/times/split")
async def record_split_time_endpoint(
    participant_id: int,
    split_time: int,
    split_number: int,
    gate_number: int,
    race_id: int,
):
    message = SplitTimeMessage(
        participant_id=participant_id,
        split_time=split_time,
        split_number=split_number,
        gate_number=gate_number,
        race_id=race_id,
    )
    await timing_service.record_split_time(message)
    return {"message": "Split time recorded successfully"}
