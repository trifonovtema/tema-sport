from fastapi import FastAPI

# from ...base.kafka import KafkaConsumerService
from .services import S3Service

app = FastAPI()

# Start Kafka consumer when the application starts
s3_service = S3Service()
# consumer_service = KafkaConsumerService(consumer_function=s3_service.handle_pdf_generation)
# consumer_service.start()
