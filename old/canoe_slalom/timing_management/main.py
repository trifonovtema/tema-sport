from fastapi import FastAPI
from .routes import router as timing_router

# from ...base.kafka import KafkaConsumerService

app = FastAPI()
app.include_router(timing_router)

# Start Kafka consumer when the application starts
# consumer_service = KafkaConsumerService()
# consumer_service.start()
