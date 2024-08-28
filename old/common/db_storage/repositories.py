from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from .models import Result
from sqlalchemy.future import select
from sqlalchemy.dialects.postgresql import insert


class ResultRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_result(self, race_id: int):
        stmt = select(Result).filter_by(race_id=race_id)
        result = await self.db.execute(stmt)
        return result.scalars().first()

    # async def create_result(self, result: Result):
    #     await self.db.add(result)
    #     await self.db.commit()
    #     await self.db.refresh(result)
    #     return result

    async def save_result(self, result: Result):
        # await self.db.commit()
        # await self.db.refresh(result)
        # return result
        # res = await self.db.query(Result).filter(Result.participant_id == result.participant_id, Result.race_id == result.race_id).first()
        # if res is None:
        #     if result.start_time is not None:
        #         res.start_time = result.start_time
        #     if result.finish_time is not None:
        #         res.finish_time = result.finish_time
        #     if res.start_time is not None and result.finish_time is not None:
        #         res.total_time = result.finish_time - res.start_time
        #     res.penalties += result.penalties
        # else:
        #     await self.db.add(result)
        # await self.db.commit()

        result_dict = {
            column.name: getattr(result, column.name)
            for column in Result.__table__.columns
        }

        # Создаем запрос на вставку
        stmt = insert(Result).values(result_dict)

        # Определяем данные для обновления при конфликте
        update_dict = {
            c.name: getattr(stmt.excluded, c.name)
            for c in stmt.table.c
            if c.name != "id"
        }

        # Указываем, что делать при конфликте
        stmt = stmt.on_conflict_do_update(
            index_elements=["race_id", "participant_id"], set_=update_dict
        )

        # Выполняем запрос
        await self.db.execute(stmt)

        # Фиксируем транзакцию
        await self.db.commit()
