from .consumer_services.consumer_service import ConsumerService
from backend.constants import KafkaTopic, GroupId
from ...kafka_service import KafkaConsumerManager

kafka_consumer_manager = KafkaConsumerManager()

kafka_consumer_manager.add_consumer(
    topic=KafkaTopic.USERS,
    group_id=GroupId.DB_STORAGE,
    consumer_service=ConsumerService(),
)

kafka_consumer_manager.add_consumer(
    topic=KafkaTopic.COMPETITIONS,
    group_id=GroupId.DB_STORAGE,
    consumer_service=ConsumerService(),
)
