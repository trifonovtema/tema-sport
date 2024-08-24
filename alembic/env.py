import asyncio

from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config


from logging.config import fileConfig

from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
from backend.settings import get_settings
from backend.core.models import Base

# from config import Settings
from sqlalchemy.schema import CreateSchema

settings = get_settings()
config = context.config
ALEMBIC_VERSION_SCHEMA = "alembic"
section = config.config_ini_section
config.set_section_option(section, "POSTGRES_PASSWORD", settings.db.PASSWORD)
config.set_section_option(section, "POSTGRES_USER", settings.db.USER)
config.set_section_option(section, "POSTGRES_DB", settings.db.NAME)
config.set_section_option(section, "POSTGRES_HOST", settings.db.HOST)
config.set_section_option(section, "POSTGRES_PORT", settings.db.PORT)
config.set_main_option("sqlalchemy.url", settings.db.get_db_url2())

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = [Base.metadata]


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_table_schema=ALEMBIC_VERSION_SCHEMA,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        version_table_schema=ALEMBIC_VERSION_SCHEMA,
    )

    connection.execute(CreateSchema(ALEMBIC_VERSION_SCHEMA, if_not_exists=True))

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
