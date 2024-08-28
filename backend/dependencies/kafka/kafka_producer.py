from backend.core.kafka.kafka_producer import KafkaProducer


async def get_client_kafka_producer(request: Request) -> KafkaProducer:
    kafka_producer = KafkaProducer()
    try:
        await kafka_producer.start()
        yield kafka_producer
    finally:
        await kafka_producer.stop()
