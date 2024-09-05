from typing import Any, Dict, Optional

from fastapi_users.models import UP

from core.config import settings


class BaseDatabase:
    async def get(self, id: settings.db.id_type.id_type) -> Optional[Any]:
        raise NotImplementedError()

    async def create(self, create_dict: Dict[str, Any]) -> Any:
        raise NotImplementedError()

    async def update(self, user: UP, update_dict: Dict[str, Any]) -> Any:
        raise NotImplementedError()

    async def delete(self, user: UP) -> None:
        raise NotImplementedError()
