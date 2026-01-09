from logging.config import fileConfig
from alembic import context
from sqlalchemy import pool

from sqlmodel import SQLModel

from app.core import engine  # nowa: F401
from app.core.entites import Building  # noqa: F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata


def include_object(object, name, type_, reflected, compare_to):
    # Ignore PostGIS / TIGER / system tables
    if reflected and (
            name.startswith("spatial_ref_sys")
            or name.startswith("tiger")
            or name.startswith("topology")
            or name.startswith("addr")
            or name.startswith("pagc")
            or name.startswith("loader")
    ):
        return False
    return True


def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            include_object=include_object
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
