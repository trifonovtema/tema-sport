from .kafka import KafkaProducerService


class BaseService:
    def __init__(self):
        self.producer_service = KafkaProducerService()

    async def record_event(self, message):
        raise NotImplementedError("This method should be overridden in derived classes")
