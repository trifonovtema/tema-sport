from ...base.services import BaseService
from .models import ParticipantMessage


class ParticipantService(BaseService):
    async def add_participant(self, message: ParticipantMessage):
        await self.producer_service.produce_message("participants", message.dict())
