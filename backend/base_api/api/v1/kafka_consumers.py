from constants import KafkaTopic, GroupId
from kafka_service import KafkaConsumerManager

kafka_consumer_manager = KafkaConsumerManager()

kafka_consumer_manager.add_consumer_websocket(
    topic=KafkaTopic.WEBSOCKET, group_id=GroupId.BASE_API
)
