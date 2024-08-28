import asyncio
from abc import ABC, abstractmethod
from typing import List, Annotated
from time import time
import uuid
from fastapi import Depends
from backend.core.kafka.kafka_producer import KafkaProducer
from backend.core.types.kafka import MessageType
from backend.dependencies.kafka.kafka_producer import get_kafka_producer
from backend.kafka import KafkaProducerService, KafkaConsumer, ConsumerServiceBase
from backend.core.schemas.kafka import KafkaMessageHeader, KafkaMessage
from backend.core.schemas.common import APIResponse
from backend.constants import KafkaTopic, APIResponseStatus


class KafkaManagerBase(ABC):
    def __init__(
        self,
        topic: KafkaTopic,
        response_topic: KafkaTopic,
        message_type: MessageType,
        producer: KafkaProducer,
    ):
        self.producer = producer
        self.topic = topic
        self.response_topic = response_topic
        self.message_type = message_type

    @staticmethod
    def generate_trace_id():
        timestamp = str(int(time() * 1000))
        uuid_part = str(uuid.uuid4())
        trace_id = f"{timestamp}-{uuid_part}"
        return trace_id

    async def send_message(self):
        header = KafkaMessageHeader(
            trace_id=self.generate_trace_id(),
            client_id=client_id,
            message_type=self.message_type,
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
