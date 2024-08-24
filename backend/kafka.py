import asyncio
from abc import ABC

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import json

from backend.base_api.v1.websocket_manager import WebSocketManager
from backend.core.schemas.kafka import KafkaMessage
from backend.settings import get_settings
from fastapi import WebSocket, WebSocketDisconnect
from backend.constants import KafkaTopic


class KafkaProducerService:
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


class ConsumerServiceBase(ABC):
    async def process_message(self, message: KafkaMessage, topic: KafkaTopic):
        raise


class KafkaConsumer:
    def __init__(
        self,
        topic: KafkaTopic,
        group_id: str,
        consumer_service: ConsumerServiceBase | None = None,
    ):
        self.topic = topic.value
        self.settings = get_settings()
        self.bootstrap_servers = self.settings.kafka.bootstrap_servers
        self.group_id = group_id
        self.consumer = AIOKafkaConsumer(
            self.topic,
            bootstrap_servers=self.settings.kafka.bootstrap_servers,
            group_id=self.group_id,
            auto_offset_reset="earliest",
        )
        self.consumer_service = consumer_service
        # self.websocket_clients: Dict[str, WebSocket] = {}
        # self.pending_messages: Dict[str, List[KafkaMessage]] = {}
        self.websocket_manager = WebSocketManager()

    async def start(self):
        await self.consumer.start()

    async def stop(self):
        await self.consumer.stop()

    async def consume_messages_websocket(self):
        try:
            print(f"consume_messages_websocket from topic - {self.topic}")
            async for msg in self.consumer:
                message = KafkaMessage.model_validate(json.loads(msg.value))
                client_id = message.header.client_id

                if client_id in self.websocket_manager.websocket_clients:
                    websocket = self.websocket_manager.websocket_clients[client_id]
                    if websocket is not None:
                        try:
                            await websocket.send_json(message.model_dump_json())
                        except WebSocketDisconnect:
                            print(f"Client {websocket.client} disconnected")
                            await self.on_websocket_disconnect(client_id, message)
                    else:
                        await self.on_websocket_disconnect(client_id, message)
                else:
                    await self.on_websocket_disconnect(client_id, message)

        except asyncio.CancelledError:
            pass

    async def on_websocket_disconnect(self, client_id: str, message: KafkaMessage):
        await self.websocket_manager.unregister_websocket(client_id)
        await self.websocket_manager.store_message_for_later_delivery(
            client_id, message
        )

    async def register_websocket(self, websocket: WebSocket, client_id: str):
        await self.websocket_manager.register_websocket(websocket, client_id)

    async def unregister_websocket(self, client_id: str):
        await self.websocket_manager.unregister_websocket(client_id)

    async def consume_messages(self):
        print(f"consume_messages from topic - {self.topic}")
        async for msg in self.consumer:
            message = KafkaMessage.model_validate(json.loads(msg.value))
            await self.consumer_service.process_message(
                message=message, topic=self.topic
            )
            await self.consumer.commit()
