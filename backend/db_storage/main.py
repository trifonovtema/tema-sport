import asyncio

from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.db_storage.v1.kafka_consumers import kafka_consumer_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous context manager to manage application lifespan events,
    such as setup at startup and cleanup at shutdown.
    """
    tasks = await kafka_consumer_manager.start_all()
    yield
    await kafka_consumer_manager.stop_all()
    for task in tasks:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass


app = FastAPI(lifespan=lifespan)
