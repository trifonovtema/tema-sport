# import asyncio
# from asyncio import tasks

import uvicorn
from fastapi import FastAPI
from base_api.api.router import router as router_api
from fastapi.responses import ORJSONResponse

# from base_api.v1.router_websocket import router as router_websocket
from contextlib import asynccontextmanager

# from base_api.api.v1.kafka_consumers import kafka_consumer_manager
from core.models import db_helper

# from actions.create_superuser import create_superuser
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous context manager to manage application lifespan events,
    such as setup at startup and cleanup at shutdown.
    """
    # user = await create_superuser()
    # tasks = await kafka_consumer_manager.start_all()
    yield
    # await kafka_consumer_manager.stop_all()
    await db_helper.dispose()
    # for task in tasks:
    #     task.cancel()
    #     try:
    #         await task
    #     except asyncio.CancelledError:
    #         pass


main_app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:5173",
]

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


main_app.include_router(
    router_api,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
