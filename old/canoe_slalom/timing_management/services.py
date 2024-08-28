from ...base.services import BaseService
from .models import StartTimeMessage, FinishTimeMessage, SplitTimeMessage


class TimingService(BaseService):
    async def record_start_time(self, message: StartTimeMessage):
        await self.producer_service.produce_message("start_times", message.dict())

    async def record_finish_time(self, message: FinishTimeMessage):
        await self.producer_service.produce_message("finish_times", message.dict())

    async def record_split_time(self, message: SplitTimeMessage):
        await self.producer_service.produce_message("split_times", message.dict())
