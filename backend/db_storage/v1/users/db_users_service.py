from fastapi import HTTPException
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy.future import select
from backend.core.schemas.old_user import (
    User,
    ProcessUser,
    DeletedUser,
    GetMessage,
    GetUsersResult,
)
from backend.core.schemas.kafka import KafkaMessage

from ..models import User as DbUser
from backend.constants import MessageType


class DbUsersService:
    async def perform_users_action(self, message: KafkaMessage, session: AsyncSession):
        return await self.user_action(header_type=message.header.message_type)(
            message, session
        )

    def user_action(self, header_type: MessageType):
        if header_type == MessageType.USERS_ADD:
            return self.add_user_to_db
        if header_type == MessageType.USERS_UPDATE:
            return self.update_user_in_db
        if header_type == MessageType.USERS_DELETE:
            return self.delete_user_in_db
        if header_type == MessageType.USERS_GET:
            return self.get_users_from_db

    @staticmethod
    async def add_user_to_db(message: KafkaMessage, session: AsyncSession):
        user = User.model_validate(ProcessUser.model_validate(message.payload).user)
        db_user = DbUser()
        user_data = user.model_dump(exclude_unset=True)
        for field, value in user_data.items():
            if field != "id":
                setattr(db_user, field, value)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        res_user = User.from_orm(db_user)
        return res_user

    @staticmethod
    async def update_user_in_db(message: KafkaMessage, session: AsyncSession):
        user_data = User.model_validate(
            ProcessUser.model_validate(message.payload).user
        )
        user_id = ProcessUser.model_validate(message.payload).id
        db_user = await session.get(DbUser, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)
        db_user.id = user_id
        print(f"Updated db_user before commit: {db_user=}")
        await session.commit()
        await session.refresh(db_user)
        print(f"Updated db_user after commit: {db_user=}")
        updated_user = User.from_orm(db_user)
        return updated_user

    @staticmethod
    async def delete_user_in_db(message: KafkaMessage, session: AsyncSession):
        user_id = ProcessUser.model_validate(message.payload).id
        db_user = await session.get(DbUser, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        await session.delete(db_user)
        await session.commit()
        return DeletedUser(id=user_id)

    @staticmethod
    async def get_users_from_db(message: KafkaMessage, session: AsyncSession):
        get_users_message = GetMessage.model_validate(message.payload)
        limit = get_users_message.limit
        skip = get_users_message.skip
        user_id = get_users_message.user_id
        stmt = select(DbUser).offset(skip).limit(limit + 1)
        result = await session.execute(stmt)
        db_users = result.scalars().all()
        next_exists = False
        if len(db_users) > limit:
            next_exists = True
            db_users = db_users[:limit]
        users = [User.from_orm(db_user) for db_user in db_users]
        res = GetUsersResult(
            users=users,
            next_exists=next_exists,
            page=(skip // limit) + 1,
            page_size=limit,
        )
        return res
