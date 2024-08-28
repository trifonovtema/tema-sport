from aiokafka import AIOKafkaConsumer
from .models import (
    StartTimeMessage,
    FinishTimeMessage,
    PenaltyMessage,
    SplitTimeMessage,
)
from .services import ResultService
import asyncio


class KafkaConsumerService:
    def __init__(self):
        self.start_consumer = AIOKafkaConsumer(
            "start_times",
            bootstrap_servers="kafka:9092",
            value_deserializer=lambda v: StartTimeMessage.parse_raw(v),
        )
        self.finish_consumer = AIOKafkaConsumer(
            "finish_times",
            bootstrap_servers="kafka:9092",
            value_deserializer=lambda v: FinishTimeMessage.parse_raw(v),
        )
        self.penalty_consumer = AIOKafkaConsumer(
            "penalties",
            bootstrap_servers="kafka:9092",
            value_deserializer=lambda v: PenaltyMessage.parse_raw(v),
        )
        self.split_consumer = AIOKafkaConsumer(
            "split_times",
            bootstrap_servers="kafka:9092",
            value_deserializer=lambda v: SplitTimeMessage.parse_raw(v),
        )
        self.result_service = ResultService()

    async def consume_start_times(self):
        await self.start_consumer.start()
        try:
            async for message in self.start_consumer:
                print(f"Start time received: {message.value}")
                await self.result_service.save_result(
                    participant_id=message.value.participant_id,
                    race_id=message.value.race_id,
                    start_time=message.value.start_time,
                )
        finally:
            await self.start_consumer.stop()

    async def consume_finish_times(self):
        await self.finish_consumer.start()
        try:
            async for message in self.finish_consumer:
                print(f"Finish time received: {message.value}")
                await self.result_service.save_result(
                    participant_id=message.value.participant_id,
                    race_id=message.value.race_id,
                    finish_time=message.value.finish_time,
                )
        finally:
            await self.finish_consumer.stop()

    async def consume_penalties(self):
        await self.penalty_consumer.start()
        try:
            async for message in self.penalty_consumer:
                print(f"Penalty received: {message.value}")
                await self.result_service.save_penalty(
                    participant_id=message.value.participant_id,
                    gate_number=message.value.gate_number,
                    penalty_time=message.value.penalty_time,
                    judge_id=message.value.judge_id,
                    comment=message.value.comment,
                    attempt_number=message.value.attempt_number,
                    race_id=message.value.race_id,
                )
        finally:
            await self.penalty_consumer.stop()

    async def consume_split_times(self):
        await self.split_consumer.start()
        try:
            async for message in self.split_consumer:
                print(f"Split time received: {message.value}")
                await self.result_service.save_split(
                    participant_id=message.value.participant_id,
                    split_time=message.value.split_time,
                    split_number=message.value.split_number,
                    gate_number=message.value.gate_number,
                    race_id=message.value.race_id,
                )
        finally:
            await self.split_consumer.stop()

    def start(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.consume_start_times())
        loop.create_task(self.consume_finish_times())
        loop.create_task(self.consume_penalties())
        loop.create_task(self.consume_split_times())
