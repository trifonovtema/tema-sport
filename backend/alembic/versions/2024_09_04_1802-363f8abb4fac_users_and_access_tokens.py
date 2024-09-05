"""users and access_tokens

Revision ID: 363f8abb4fac
Revises: b7d6bfbaae14
Create Date: 2024-09-04 18:02:29.117978

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy

# revision identifiers, used by Alembic.
revision: str = "363f8abb4fac"
down_revision: Union[str, None] = "b7d6bfbaae14"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), nullable=False),
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
    op.create_table(
        "access_tokens",
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("token", sa.String(length=43), nullable=False),
        sa.Column(
            "created_at",
            fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["tema_sport.users.id"],
            name=op.f("fk_access_tokens_user_id_users"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("token", name=op.f("pk_access_tokens")),
        schema="tema_sport",
    )
    op.create_index(
        op.f("ix_tema_sport_access_tokens_created_at"),
        "access_tokens",
        ["created_at"],
        unique=False,
        schema="tema_sport",
    )


def downgrade() -> None:
    op.drop_index(
        op.f("ix_tema_sport_access_tokens_created_at"),
        table_name="access_tokens",
        schema="tema_sport",
    )
    op.drop_table("access_tokens", schema="tema_sport")
    op.drop_index(
        op.f("ix_tema_sport_users_email"),
        table_name="users",
        schema="tema_sport",
    )
    op.drop_table("users", schema="tema_sport")
