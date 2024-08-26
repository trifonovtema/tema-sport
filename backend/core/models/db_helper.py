from typing import AsyncGenerator


from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
)

from backend.settings import get_settings


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        pool_size: int = 5,
        max_overflow: int = 10,
    ) -> None:
        print(f"{url=}")
        print(f"{settings.db.PASSWORD=}")
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

    # Use for more control
    # @contextlib.asynccontextmanager
    # async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
    #     session = self.session_factory()
    #     try:
    #         yield session
    #     except Exception as e:
    #         logger.error("Session rollback due to error: %s", e)
    #         await session.rollback()
    #         raise
    #     finally:
    #         await session.close()
    #         logger.info("Session closed")


settings = get_settings()

db_helper = DatabaseHelper(
    url=settings.db.get_db_url(),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
