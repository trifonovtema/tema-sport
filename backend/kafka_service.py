import asyncio
from abc import ABC, abstractmethod
from typing import List
from time import time
import uuid
from backend.kafka import KafkaProducerService, KafkaConsumer, ConsumerServiceBase
from backend.core.schemas.kafka import KafkaMessageHeader, KafkaMessage
from backend.core.schemas.common import APIResponse
from backend.constants import KafkaTopic, MessageType, APIResponseStatus


class KafkaServiceBase(ABC):
    def __init__(
        self,
        topic: KafkaTopic,
        response_topic: KafkaTopic,
        message_type_add: MessageType,
        message_type_update: MessageType,
        message_type_delete: MessageType,
        message_type_get: MessageType,
    ):
        self.producer_service = KafkaProducerService()
        self.topic = topic
        self.response_topic = response_topic
        self.message_type_add = message_type_add
        self.message_type_update = message_type_update
        self.message_type_delete = message_type_delete
        self.message_type_get = message_type_get

    @staticmethod
    def generate_trace_id():
        timestamp = str(int(time() * 1000))
        uuid_part = str(uuid.uuid4())
        trace_id = f"{timestamp}-{uuid_part}"
        return trace_id

    @abstractmethod
    def create_payload(self, **kwargs) -> dict:
        raise

    async def process(self, client_id: str, message_type: MessageType, **kwargs):
        trace_id = self.generate_trace_id()
        header = KafkaMessageHeader(
            trace_id=trace_id,
            client_id=client_id,
            message_type=message_type,
            response_topic=self.response_topic,
        )
        payload = self.create_payload(**kwargs)
        kafka_message = KafkaMessage(header=header, payload=payload)

        await self.producer_service.produce_message(
            topic=self.topic, value=kafka_message
        )
        return APIResponse(
            trace_id=trace_id, status=APIResponseStatus.SUCCESS, message=message_type
        )

    async def add(self, **kwargs):
        return await self.process(message_type=self.message_type_add, **kwargs)

    async def update(self, **kwargs):
        return await self.process(message_type=self.message_type_update, **kwargs)

    async def delete(self, **kwargs):
        return await self.process(message_type=self.message_type_delete, **kwargs)

    async def get(self, client_id: str, skip: int = 0, limit: int = 1, **kwargs):
        trace_id = self.generate_trace_id()
        header = KafkaMessageHeader(
            trace_id=trace_id,
            client_id=client_id,
            type=self.message_type_get,
            response_topic=self.response_topic,
        )

        payload = self.create_payload(skip=skip, limit=limit, **kwargs)
        kafka_message = KafkaMessage(header=header, payload=payload)
        await self.producer_service.produce_message(
            topic=self.topic, value=kafka_message
        )
        return APIResponse(
            trace_id=trace_id,
            status=APIResponseStatus.SUCCESS,
            message=self.message_type_get,
        )


class KafkaConsumerManager:
    def __init__(self):
        self.consumers: List[KafkaConsumer] = []
        self.consumer_websocket: KafkaConsumer = None

    def add_consumer(
        self,
        topic: KafkaTopic,
        group_id: str,
        consumer_service: ConsumerServiceBase | None = None,
    ):
        consumer = KafkaConsumer(
            topic=topic, group_id=group_id, consumer_service=consumer_service
        )
        self.consumers.append(consumer)

    def add_consumer_websocket(
        self,
        topic: KafkaTopic,
        group_id: str,
        consumer_service: ConsumerServiceBase | None = None,
    ):
        print("add_consumer_websocket")
        consumer = KafkaConsumer(
            topic=topic, group_id=group_id, consumer_service=consumer_service
        )
        self.consumer_websocket = consumer

    async def start_consume_all(self):
        if self.consumers == []:
            return []
        for consumer in self.consumers:
            await consumer.start()
        tasks = [
            asyncio.create_task(consumer.consume_messages())
            for consumer in self.consumers
        ]
        return tasks

    async def start_consume_websocket_all(self):
        if self.consumer_websocket is None:
            return []
        await self.consumer_websocket.start()
        tasks = [
            asyncio.create_task(self.consumer_websocket.consume_messages_websocket())
        ]
        return tasks

    async def start_all(self):
        tasks_consume = await self.start_consume_all()
        tasks_consume_websocket = await self.start_consume_websocket_all()
        return tasks_consume + tasks_consume_websocket

    async def stop_all(self):
        for consumer in self.consumers:
            await consumer.stop()
