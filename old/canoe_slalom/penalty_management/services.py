from ...base.services import BaseService
from .models import PenaltyMessage


class PenaltyService(BaseService):
    async def add_penalty(self, message: PenaltyMessage):
        await self.producer_service.produce_message("penalties", message.dict())
