import logging
from functools import lru_cache
from dotenv import load_dotenv, find_dotenv
from pydantic import PostgresDsn, RedisDsn, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL
from devtools import debug
from core.types.id import IdType, IdTypeUuid, IdTypeInt

logger = logging.getLogger(__name__)

APP_PREFIX = "APP_CONFIG__"

dotenv_path = find_dotenv()
if load_dotenv(dotenv_path):
    print(f".env file loaded from {dotenv_path}")
else:
    print(f"Failed to load .env file from {dotenv_path}")


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"
    auth: str = "/auth"
    runs: str = "/runs"
    races: str = "/races"
    course_elements: str = "/course_elements"
    gates: str = "/gates"
    splits: str = "/splits"
    starts: str = "/starts"
    finishes: str = "/finishes"
    competition_owners: str = "/competition_owners"
    finish_runs: str = "/finish_runs"
    race_registrations: str = "/race_registrations"
    split_runs: str = "/split_runs"
    competitor_medal_groups: str = "/competitor_medal_groups"
    competitions: str = "/competitions"
    agg_race_results: str = "/agg_race_results"
    competition_scoring_rules: str = "/competition_scoring_rules"
    start_runs: str = "/start_runs"
    competitor_runs: str = "/competitor_runs"
    competitors: str = "/competitors"
    competition_results: str = "/competition_results"
    race_stages: str = "/race_stages"
    bib_competitors: str = "/bib_competitors"
    bib_athletes: str = "/bib_athletes"
    competition_registered_users: str = "/competition_registered_users"
    gate_runs: str = "/gate_runs"
    judgement_groups: str = "/judgement_groups"
    medal_groups: str = "/medal_groups"
    bibs: str = "/bibs"
    race_classes: str = "/race_classes"
    agg_run_results: str = "/agg_run_results"
    athletes: str = "/athletes"
    user_profiles: str = "/user_profiles"
    scoring_rules: str = "/scoring_rules"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

    @property
    def bearer_token_url(self) -> str:
        # /v1/auth/jwt/login
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/jwt/login")
        path = "".join(parts)
        return path.removeprefix("/")


class KafkaConfig(BaseModel):
    # model_config = SettingsConfigDict(
    #     env_file=(".env.template", ".env"),
    #     case_sensitive=False,
    #     env_nested_delimiter="__",
    #     env_prefix=APP_PREFIX + "KAFKA__",
    #     extra="ignore",
    # )
    SERVER: str
    PORT: int

    @property
    def bootstrap_servers(self) -> str:
        return f"{self.SERVER}:{self.PORT}"


class RedisConfig(BaseModel):
    HOST: str
    PORT: str

    def get_redis_url(self) -> RedisDsn:
        return URL.create(drivername="redis", host=self.HOST, port=int(self.PORT))


class DatabaseConfig(BaseModel):
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

    id_type: str = "uuid"  # "int"

    @property
    def id_type_class(self) -> IdType:
        if self.id_type == "uuid":
            return IdTypeUuid()
        elif self.id_type == "int":
            return IdTypeInt()
        else:
            raise ValueError(f"Unsupported id_type: {self.id_type}")

    def get_db_url(self) -> URL:
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


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix=APP_PREFIX,
        extra="ignore",
    )
    db: DatabaseConfig
    kafka: KafkaConfig
    redis: RedisConfig
    access_token: AccessToken
    api: ApiPrefix = ApiPrefix()
    run: RunConfig = RunConfig()


@lru_cache
def get_settings() -> Settings:
    res = Settings()
    debug(res)
    return Settings()


settings = get_settings()
