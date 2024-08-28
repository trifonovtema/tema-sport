from typing import Type, Sequence
from fastapi_users import models, schemas
from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.manager import UserManagerDependency

from backend.core.kafka_fastapi_users.register import get_register_router


class KafkaFastAPIUsers(FastAPIUsers):

    def __init__(
        self,
        get_user_manager: UserManagerDependency[models.UP, models.ID],
        auth_backends: Sequence[AuthenticationBackend],
    ):
        super().__init__(get_user_manager, auth_backends)

    def get_register_router(
        self, user_schema: Type[schemas.U], user_create_schema: Type[schemas.UC]
    ) -> APIRouter:
        """
        Return a router with a register route.

        :param user_schema: Pydantic schema of a public user.
        :param user_create_schema: Pydantic schema for creating a user.
        """
        return get_register_router(
            self.get_user_manager, user_schema, user_create_schema
        )
