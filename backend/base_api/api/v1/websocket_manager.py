import json

from backend.core.schemas.kafka import KafkaMessage
from backend.settings import get_settings
from fastapi import WebSocket, WebSocketDisconnect
from redis.asyncio import Redis


class WebSocketManager:
    def __init__(self):
        self.websocket_clients = {}
        self.settings = get_settings()
        self.redis = Redis(host=self.settings.redis.HOST, port=self.settings.redis.PORT)

    async def register_websocket(self, websocket: WebSocket, client_id: str):
        self.websocket_clients[client_id] = websocket
        await self.deliver_pending_messages(client_id=client_id, websocket=websocket)

    async def unregister_websocket(self, client_id: str):
        if client_id in self.websocket_clients:
            del self.websocket_clients[client_id]

    async def store_message_for_later_delivery(
        self, client_id: str, message: KafkaMessage
    ):
        print(f"store_message_for_later_delivery - {message}")
        await self.redis.rpush(
            f"pending_messages:{client_id}", message.model_dump_json()
        )

    async def deliver_pending_messages(self, client_id: str, websocket: WebSocket):
        while True:
            message_json = await self.redis.lpop(f"pending_messages:{client_id}")
            if message_json is None:
                break

            message_dict = json.loads(message_json.decode("utf-8"))
            message = KafkaMessage.model_validate(message_dict)

            try:
                await websocket.send_json(message.model_dump_json())
                print(f"Delivered message: {message}")
            except WebSocketDisconnect:
                print(f"Failed to deliver message to {client_id}")
                await self.redis.lpush(f"pending_messages:{client_id}", message_json)
                break
