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


# from fastapi import FastAPI
# from starlette.websockets import WebSocket
#
# app = FastAPI()
#
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket) -> None:
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")
# You can use the async for notation:
#
# from fastapi import FastAPI
# from starlette.websockets import WebSocket
#
# app = FastAPI()
#
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket) -> None:
#     await websocket.accept()
#     async for data in websocket.iter_text():
#         await websocket.send_text(f"Message text was: {data}")
