import logging
from functools import lru_cache

from dotenv import find_dotenv, load_dotenv

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from sqlalchemy.engine import URL
import os

logger = logging.getLogger(__name__)

load_dotenv()


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str
    DB_PORT: str

    # model_config = SettingsConfigDict(env_file=DOTENV,
    #                                   env_file_encoding="utf-8",
    #                                   extra='ignore')

    def get_db_url(self) -> PostgresDsn:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            database=self.DB_NAME,
            port=int(self.DB_PORT),
            # query={"sslmode": "require"}
        )


@lru_cache
def get_settings():
    return Settings()
