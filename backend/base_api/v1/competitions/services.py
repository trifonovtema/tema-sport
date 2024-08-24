from backend.kafka_service import KafkaServiceBase
from backend.core.schemas.run import ProcessCompetition, Competition

from uuid import UUID
from backend.constants import KafkaTopic, MessageType


class KafkaCompetitionsService(KafkaServiceBase):
    def __init__(self):
        super().__init__(
            topic=KafkaTopic.COMPETITIONS,
            response_topic=KafkaTopic.WEBSOCKET,
            message_type_add=MessageType.COMPETITIONS_ADD,
            message_type_update=MessageType.COMPETITIONS_UPDATE,
            message_type_delete=MessageType.COMPETITIONS_DELETE,
            message_type_get=MessageType.COMPETITIONS_GET,
        )

    def create_payload(
        self,
        competition: Competition | None = None,
        competition_id: UUID | None = None,
        **kwargs
    ):
        return ProcessCompetition(id=competition_id, competition=competition)
