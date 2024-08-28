import logging

from fastapi import APIRouter, Depends, HTTPException, Query

from .db_session import DBSessionDep

# from ...users.crud import get_current_user
# from ...users.models import User
# from . import schemas
# from .crud import PipelineStateUpdater, PipelineStateRetriever  # get_pipeline_state, set_pipeline_state
from .services import ResultService

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/competitions/result")
async def create_competition(
    participant_id: int,
    race_id: int,
    start_time: int,
    finish_time: int,
    penalties: int,
    db: DBSessionDep,
):
    service = ResultService(db)
    return await service.save_result(
        participant_id=participant_id,
        race_id=race_id,
        start_time=start_time,
        finish_time=finish_time,
        penalties=penalties,
    )


@router.get("/competitions/{race_id}")
async def get_competition(race_id: int, db: DBSessionDep):
    service = ResultService(db)
    return await service.get_result(race_id)
