from fastapi import FastAPI
from .router import router

# from .kafka_consumer import KafkaConsumerService
from .database import sessionmanager

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await sessionmanager.create_tables()


# Create database tables

# Start Kafka consumers when the application starts
# consumer_service = KafkaConsumerService()
# consumer_service.start()
