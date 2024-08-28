from ...base.services import BaseService
from .models import CompetitionMessage


class CompetitionService(BaseService):
    async def start(self):
        await self.producer_service.start()

    async def create_competition(self, message: CompetitionMessage):
        await self.producer_service.produce_message(
            "competitions", message.model_dump()
        )


competition_service = CompetitionService()


def get_competition_service():
    return competition_service
