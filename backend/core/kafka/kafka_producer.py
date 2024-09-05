from aiokafka import AIOKafkaProducer
import json

from backend.core.schemas.kafka import KafkaMessage
from core.config import get_settings
from backend.constants import KafkaTopic


class KafkaProducer:
    def __init__(self):
        self.producer = None
        self.settings = get_settings()
        self.bootstrap_servers = self.settings.kafka.bootstrap_servers

    async def start(self):
        if not self.producer:
            self.producer = AIOKafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8"),
                acks="all",
            )
        await self.producer.start()

    async def produce_message(self, topic: KafkaTopic, value: KafkaMessage, **kwargs):
        if not self.producer:
            await self.start()
        await self.producer.send_and_wait(
            topic.value, value=value.model_dump(), **kwargs
        )

    async def stop(self):
        if self.producer:
            await self.producer.stop()
