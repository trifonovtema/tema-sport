from fastapi_users.authentication import BearerTransport

from backend.settings import get_settings

settings = get_settings()
bearer_transport = BearerTransport(
    tokenUrl=settings.base_api.bearer_token_url,
)
