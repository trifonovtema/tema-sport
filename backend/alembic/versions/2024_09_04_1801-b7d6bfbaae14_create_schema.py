"""create schema

Revision ID: b7d6bfbaae14
Revises:
Create Date: 2024-09-04 18:01:04.789790

"""

from typing import Sequence, Union

from alembic import op
from core.config import settings, logger

# revision identifiers, used by Alembic.
revision: str = "b7d6bfbaae14"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(f"create schema if not exists {settings.db.SCHEMA}")


def downgrade() -> None:
    op.execute(f"drop schema if exists {settings.db.SCHEMA}")
