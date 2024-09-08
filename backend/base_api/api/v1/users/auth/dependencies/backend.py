from fastapi_users.authentication import AuthenticationBackend

from base_api.api.v1.users.auth.transport import bearer_transport
from .strategy import get_database_strategy

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
