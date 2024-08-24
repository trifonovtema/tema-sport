from backend.kafka import ConsumerServiceBase
from backend.core.schemas.kafka import KafkaMessage
from ..services import DbService


class ConsumerService(ConsumerServiceBase):
    def __init__(self):
        self.db_service = DbService()

    async def process_message(self, message: KafkaMessage, topic: str):
        await self.db_service.perform_action(message=message, topic=topic)
