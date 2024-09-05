import contextlib
import logging
from typing import Any, AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base, DeclarativeMeta

from core.config import get_settings

logger = logging.getLogger(__name__)
Base: DeclarativeMeta = declarative_base()


class DatabaseSessionManager:
    """
    Manages database sessions and connections asynchronously.
    This class provides methods to create and manage database sessions
    and connections using SQLAlchemy's async capabilities.
    """

    def __init__(self, host: str, engine_kwargs: dict[str, Any]):
        """
        Initializes the database session manager with the given database host
        and engine configuration.

        :param host: Database connection URL.
        :param engine_kwargs: A dictionary of additional engine options.
        """

        logger.info(f"host={host}")
        logger.info(f"engine_kwargs={engine_kwargs}")
        self._engine = create_async_engine(host, **engine_kwargs)
        self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)

    async def close(self):
        """
        Closes the database engine and disposes of any connection pools.
        """
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self._engine.dispose()

        self._engine = None
        self._sessionmaker = None

    def get_engine(self):
        return self._engine

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        """
        Asynchronous context manager for database connections.
        Ensures that the database connection is properly closed after use.

        :yields: An instance of AsyncConnection.
        """
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        """
        Asynchronous context manager for database sessions.
        Manages the lifecycle of a session, including rollback and close in case of an exception.

        :yields: An instance of AsyncSession.
        """
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def create_tables(self):
        async with self._engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)


# Instantiate the session manager with database URL and echo flag.
sessionmanager = DatabaseSessionManager(get_settings().db.get_db_url(), {"echo": True})


async def get_db():
    """
    Asynchronous generator that provides a database session.
    """
    async with sessionmanager.session() as session:
        yield session
