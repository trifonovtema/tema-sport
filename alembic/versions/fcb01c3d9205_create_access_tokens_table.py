"""create access_tokens table

Revision ID: fcb01c3d9205
Revises: 85380b5ae9d9
Create Date: 2024-08-26 02:01:13.250331

"""

from typing import Sequence, Union
import fastapi_users_db_sqlalchemy

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fcb01c3d9205"
down_revision: Union[str, None] = "85380b5ae9d9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        "access_tokens",
        sa.Column("user_id", sa.Integer(), nullable=False),
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
