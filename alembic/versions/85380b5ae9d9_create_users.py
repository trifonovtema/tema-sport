"""create users

Revision ID: 85380b5ae9d9
Revises:
Create Date: 2024-08-26 01:12:27.775400

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "85380b5ae9d9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("create schema if not exists tema_sport")
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        schema="tema_sport",
    )
    op.create_index(
        op.f("ix_tema_sport_users_email"),
        "users",
        ["email"],
        unique=True,
        schema="tema_sport",
    )


def downgrade() -> None:
    op.drop_index(
        op.f("ix_tema_sport_users_email"), table_name="users", schema="tema_sport"
    )
    op.drop_table("users", schema="tema_sport")
    op.execute("drop schema if exists tema_sport")
