import uuid
from time import time
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import json
from ..settings import get_settings
from fastapi import WebSocket, WebSocketDisconnect
from .services import DbService
from ..schemas import UserKafkaMessage, User, KafkaMessageHeader, KafkaMessage


class KafkaProducerService:
    def __init__(self):
        self.producer = None
        self.settings = get_settings()
        print(f"{self.settings=}")
        self.bootstrap_servers = self.settings.kafka.bootstrap_servers
        print(f"{self.bootstrap_servers=}")

    async def start(self):
        if not self.producer:
            self.producer = AIOKafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            )
        await self.producer.start()

    @staticmethod
    def generate_trace_id():
        timestamp = str(int(time() * 1000))
        uuid_part = str(uuid.uuid4())
        trace_id = f"{timestamp}-{uuid_part}"
        return trace_id

    async def produce_message(self, topic, value, headers, **kwargs):
        if not self.producer:
            await self.start()
        trace_id = self.generate_trace_id()
        headers = [
            ("X-Trace-Id", trace_id.encode("utf-8")),
            ("Message-Type", message_type.encode("utf-8")),
            ("Content-Type", b"application/json"),
        ]
        await self.producer.send_and_wait(topic, value=value, headers=headers, **kwargs)
        return trace_id

    async def stop(self):
        if self.producer:
            await self.producer.stop()


class KafkaConsumer:
    def __init__(self, topic: str, group_id: str):
        self.topic = topic
        self.settings = get_settings()
        self.bootstrap_servers = self.settings.kafka.bootstrap_servers
        self.group_id = group_id
        self.consumer = AIOKafkaConsumer(
            self.topic,
            bootstrap_servers=self.settings.kafka.bootstrap_servers,
            group_id=self.group_id,
            auto_offset_reset="earliest",
        )
        self.db_service = DbService()

    async def start(self):
        print("start")
        await self.consumer.start()

    async def stop(self):
        print("stop")

        await self.consumer.stop()

    async def consume_messages(self):
        print("consume_messages")
        async for msg in self.consumer:

            message = KafkaMessage.model_validate(json.loads(msg.value))
            await self.db_service.perform_db_action(message)

            # message = json.loads(msg.value.decode('utf-8'))
            #
            # trace_id = None
            # for header_key, header_value in msg.headers:
            #     if header_key == 'X-Trace-Id':
            #         trace_id = header_value.decode('utf-8')
            #         break
            #
            # print(f"""Message: {message.get("name")}""")
            # print(f"Trace ID: {trace_id}")
            # res = {"trace_id": trace_id, "message": message.get("name")}
            # await websocket.send_json(res)
