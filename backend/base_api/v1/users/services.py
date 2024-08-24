from backend.kafka_service import KafkaServiceBase
from backend.core.schemas.old_user import AddUser, User, ProcessUser
from uuid import UUID
from backend.constants import KafkaTopic, MessageType


class KafkaUsersService(KafkaServiceBase):
    def __init__(self):
        super().__init__(
            topic=KafkaTopic.USERS,
            response_topic=KafkaTopic.WEBSOCKET,
            message_type_add=MessageType.USERS_ADD,
            message_type_update=MessageType.USERS_UPDATE,
            message_type_delete=MessageType.USERS_DELETE,
            message_type_get=MessageType.USERS_GET,
        )

    def create_payload(
        self, user: AddUser | User | None = None, user_id: UUID | None = None, **kwargs
    ):
        return ProcessUser(id=user_id, user=user)
