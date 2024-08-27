"""create users

Revision ID: 85380b5ae9d9
Revises:
Create Date: 2024-08-26 01:12:27.775400

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "85380b5ae9d9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("create schema if not exists tema_sport")


def downgrade() -> None:
    op.execute("drop schema if exists tema_sport")
