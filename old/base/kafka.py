from aiokafka import AIOKafkaProducer
import json


class KafkaProducerService:
    def __init__(self):
        self.producer = None

    async def start(self):
        if not self.producer:
            self.producer = AIOKafkaProducer(
                bootstrap_servers="kafka:9092",
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            )
        await self.producer.start()

    async def produce_message(self, topic, message, **kwargs):
        if not self.producer:
            await self.start()
        await self.producer.send_and_wait(topic, value=message, **kwargs)

    async def stop(self):
        if self.producer:
            await self.producer.stop()
