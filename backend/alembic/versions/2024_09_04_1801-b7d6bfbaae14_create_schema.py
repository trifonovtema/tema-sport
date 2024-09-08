"""create schema

Revision ID: b7d6bfbaae14
Revises:
Create Date: 2024-09-04 18:01:04.789790

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "b7d6bfbaae14"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("create schema if not exists tema_sport")


def downgrade() -> None:
    op.execute("drop schema if exists tema_sport")
