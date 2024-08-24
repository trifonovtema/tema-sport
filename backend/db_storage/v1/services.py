from typing import Any

from backend.core.schemas.kafka import (
    KafkaMessage,
    ResponseMessage,
    KafkaMessageHeader,
)

from backend.kafka import KafkaProducerService
from backend.constants import KafkaTopic, ResponseStatus
from .users.db_users_service import DbUsersService
from ...core.models.db_helper import DatabaseHelper


class DbService:
    def __init__(self):
        self.database_helper = DatabaseHelper
        self.producer_service = KafkaProducerService()
        self.db_users_service = DbUsersService()

    async def produce_response(self, res: Any, header: KafkaMessageHeader):
        message_body = ResponseMessage(payload=res, status=ResponseStatus.SUCCESS)
        result_message = KafkaMessage(header=header, payload=message_body)
        response_topic = header.response_topic
        res = await self.producer_service.produce_message(
            topic=response_topic, value=result_message
        )

        print(f"{res=}")

    async def perform_action(self, message: KafkaMessage, topic: str):
        print("perform_action")
        header = message.header
        res = None
        async for session in self.database_helper.session_getter():
            if topic == KafkaTopic.USERS:
                res = await self.db_users_service.perform_users_action(
                    message=message, session=session
                )

                print(f"1111111{res=}")
        await self.produce_response(res=res, header=header)
