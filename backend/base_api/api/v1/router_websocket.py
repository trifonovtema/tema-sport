from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from .kafka_consumers import kafka_consumer_manager

router = APIRouter()


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    print(f"{websocket.client=}")
    await kafka_consumer_manager.consumer_websocket.register_websocket(
        websocket=websocket, client_id=client_id
    )
    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        print("WebSocket disconnected")

    finally:
        await kafka_consumer_manager.consumer_websocket.unregister_websocket(
            client_id=client_id
        )
