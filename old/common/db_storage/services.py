from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from .repositories import ResultRepository
from .models import Result


class ResultService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.result_repository = ResultRepository(db)

    async def get_result(self, race_id: int):
        return await self.result_repository.get_result(race_id)

    async def save_result(
        self,
        participant_id: int,
        race_id: int,
        start_time: int = None,
        finish_time: int = None,
        penalties: int = 0,
    ):
        result = await self.result_repository.get_result(race_id)
        if result:
            if start_time is not None:
                result.start_time = start_time
            if finish_time is not None:
                result.finish_time = finish_time
            if start_time is not None and finish_time is not None:
                result.total_time = finish_time - start_time
            result.penalties += penalties
            # return await self.result_repository.save_result(result)
        else:
            result = Result(
                participant_id=participant_id,
                race_id=race_id,
                start_time=start_time,
                finish_time=finish_time,
                total_time=(
                    finish_time - start_time if start_time and finish_time else None
                ),
                penalties=penalties,
            )
        return await self.result_repository.save_result(result)


#
#
#
# class ResultService:
#     async def get_result(self, participant_id: int, race_id: int):
#         async with SessionLocal() as db:
#             result = await db.query(Result).filter(Result.participant_id == participant_id, Result.race_id == race_id).first()
#             return result
#
#     async def save_result(self, participant_id: int, race_id: int, start_time: int = None, finish_time: int = None, penalties: int = 0):
#         async with SessionLocal() as db:
#             result = await db.query(Result).filter(Result.participant_id == participant_id, Result.race_id == race_id).first()
#             if result:
#                 if start_time is not None:
#                     result.start_time = start_time
#                 if finish_time is not None:
#                     result.finish_time = finish_time
#                 if start_time is not None and finish_time is not None:
#                     result.total_time = finish_time - start_time
#                 result.penalties += penalties
#             else:
#                 new_result = Result(
#                     participant_id=participant_id,
#                     race_id=race_id,
#                     start_time=start_time,
#                     finish_time=finish_time,
#                     total_time=(finish_time - start_time if start_time and finish_time else None),
#                     penalties=penalties
#                 )
#                 db.add(new_result)
#             await db.commit()
#
#     async def save_penalty(self, participant_id: int, gate_number: int, penalty_time: int, judge_id: int, comment: str, attempt_number: int, race_id: int):
#         async with SessionLocal() as db:
#             penalty = Penalty(
#                 participant_id=participant_id,
#                 gate_number=gate_number,
#                 penalty_time=penalty_time,
#                 judge_id=judge_id,
#                 comment=comment,
#                 attempt_number=attempt_number,
#                 race_id=race_id
#             )
#             db.add(penalty)
#             await db.commit()
#
#     async def save_split(self, participant_id: int, split_time: int, split_number: int, gate_number: int, race_id: int):
#         async with SessionLocal() as db:
#             split = Split(
#                 participant_id=participant_id,
#                 split_time=split_time,
#                 split_number=split_number,
#                 gate_number=gate_number,
#                 race_id=race_id
#             )
#             db.add(split)
#             await db.commit()
