import logging
from functools import lru_cache
from dotenv import load_dotenv, find_dotenv
from pydantic import PostgresDsn, RedisDsn, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL

from backend.core.types.id import IdType, IdTypeUuid

logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())


class BaseApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"
    auth: str = "/auth"


class BaseApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: BaseApiV1Prefix = BaseApiV1Prefix()

    @property
    def bearer_token_url(self) -> str:
        # /v1/auth/jwt/login
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/jwt/login")
        path = "".join(parts)
        return path.removeprefix("/")


class KafkaConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="KAFKA__",
        extra="ignore",
    )
    SERVER: str
    PORT: int

    @property
    def bootstrap_servers(self) -> str:
        return f"{self.SERVER}:{self.PORT}"


class RedisConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="REDIS__",
        extra="ignore",
    )
    HOST: str
    PORT: str

    def get_redis_url(self) -> RedisDsn:
        return URL.create(drivername="redis", host=self.HOST, port=int(self.PORT))


class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="DB__",
        extra="ignore",
    )
    USER: str
    PASSWORD: str
    HOST: str
    NAME: str
    PORT: str
    SCHEMA: str

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    id_type: IdType = IdTypeUuid()

    def get_db_url(self) -> PostgresDsn:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            database=self.NAME,
            port=int(self.PORT),
            # query={"sslmode": "require"}
        )

    def get_db_url2(self) -> PostgresDsn:
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class AccessToken(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="ACCESS_TOKEN__",
        extra="ignore",
    )
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    db: DatabaseConfig = DatabaseConfig()
    kafka: KafkaConfig = KafkaConfig()
    redis: RedisConfig = RedisConfig()
    access_token: AccessToken = AccessToken()
    base_api: BaseApiPrefix = BaseApiPrefix()

    # model_config = SettingsConfigDict(env_file=DOTENV,
    #                                   env_file_encoding="utf-8",
    #                                   extra='ignore')


@lru_cache
def get_settings():
    res = Settings()
    print(f"{res.redis.get_redis_url()=}")
    return Settings()
