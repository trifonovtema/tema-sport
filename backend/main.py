import asyncio

import uvicorn
from fastapi import FastAPI
from backend.base_api.api.router import router as router_api

# from backend.base_api.v1.router_websocket import router as router_websocket
from contextlib import asynccontextmanager
from backend.base_api.api.v1.kafka_consumers import kafka_consumer_manager
from backend.core.models import db_helper
from backend.actions.create_superuser import create_superuser
from backend.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous context manager to manage application lifespan events,
    such as setup at startup and cleanup at shutdown.
    """
    user = await create_superuser()
    tasks = await kafka_consumer_manager.start_all()
    yield
    await kafka_consumer_manager.stop_all()
    await db_helper.dispose()
    for task in tasks:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass


app = FastAPI(lifespan=lifespan)
app.include_router(router_api)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
