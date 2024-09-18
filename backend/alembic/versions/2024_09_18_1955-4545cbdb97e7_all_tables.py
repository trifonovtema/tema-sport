"""all tables

Revision ID: 4545cbdb97e7
Revises: b7d6bfbaae14
Create Date: 2024-09-18 19:55:17.313737

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy

# revision identifiers, used by Alembic.
revision: str = "4545cbdb97e7"
down_revision: Union[str, None] = "b7d6bfbaae14"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "agg_race_results",
        sa.Column("competitor_id", sa.Uuid(), nullable=True),
        sa.Column("run_time", sa.BigInteger(), nullable=True),
        sa.Column("total_penalty", sa.BigInteger(), nullable=True),
        sa.Column("total_time", sa.BigInteger(), nullable=True),
        sa.Column("race_id", sa.Uuid(), nullable=True),
        sa.Column("race_class_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_agg_race_results")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "agg_run_results",
        sa.Column("run_id", sa.Uuid(), nullable=True),
        sa.Column("athlete_id", sa.Uuid(), nullable=True),
        sa.Column("run_time", sa.BigInteger(), nullable=True),
        sa.Column("total_penalty", sa.Integer(), nullable=True),
        sa.Column("total_time", sa.BigInteger(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_agg_run_results")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "athletes",
        sa.Column("competition_registered_user_id", sa.Uuid(), nullable=True),
        sa.Column("race_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_athletes")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "bib_athletes",
        sa.Column("athlete_id", sa.Uuid(), nullable=True),
        sa.Column("bib_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_bib_athletes")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "bibs",
        sa.Column("bib_number", sa.Integer(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_bibs")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "bibs_competitiors",
        sa.Column("bib_id", sa.Uuid(), nullable=True),
        sa.Column("competitor_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_bibs_competitiors")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "competition_owners",
        sa.Column("competition_id", sa.Uuid(), nullable=True),
        sa.Column("user_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competition_owners")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "competition_registered_users",
        sa.Column("user_id", sa.Uuid(), nullable=True),
        sa.Column("competition_id", sa.Uuid(), nullable=True),
        sa.Column("type", sa.Text(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competition_registered_users")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "competition_results",
        sa.Column("competition_id", sa.Uuid(), nullable=True),
        sa.Column("competitor_id", sa.Uuid(), nullable=True),
        sa.Column("run_time", sa.Integer(), nullable=True),
        sa.Column("total_penalty", sa.Integer(), nullable=True),
        sa.Column("total_time", sa.Integer(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competition_results")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "competition_scoring_rules",
        sa.Column("competition_id", sa.Uuid(), nullable=True),
        sa.Column("calculated_by_rule", sa.Text(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competition_scoring_rules")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "competitions",
        sa.Column("name", sa.Text(), nullable=True),
        sa.Column("scoring_rules_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competitions")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "competitor_runs",
        sa.Column("competitor_id", sa.Uuid(), nullable=True),
        sa.Column("scheduled_time", sa.DateTime(timezone=True), nullable=True),
        sa.Column("run_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competitor_runs")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "competitors",
        sa.Column("race_class_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competitors")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "competitors_medal_groups",
        sa.Column("competitor_id", sa.Uuid(), nullable=True),
        sa.Column("medal_group_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competitors_medal_groups")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "course_elements",
        sa.Column("race_id", sa.Uuid(), nullable=True),
        sa.Column("number", sa.Integer(), nullable=True),
        sa.Column(
            "type",
            sa.Enum(
                "GATE",
                "SPLIT",
                "START",
                "FINISH",
                name="course_element_type",
                schema="tema_sport_dev",
            ),
            nullable=True,
        ),
        sa.Column("judgement_group_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_course_elements")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "finishes",
        sa.Column("course_element_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_finishes")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "finishes_runs",
        sa.Column("finish_id", sa.Uuid(), nullable=True),
        sa.Column("competitor_run_id", sa.Uuid(), nullable=True),
        sa.Column("finish_time", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_finishes_runs")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "gates",
        sa.Column("course_element_id", sa.Uuid(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=True),
        sa.Column(
            "type",
            sa.Enum(
                "UPSTREAM",
                "DOWNSTREAM",
                name="course_element_type",
                schema="tema_sport_dev",
            ),
            nullable=True,
        ),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_gates")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "gates_runs",
        sa.Column("gate_id", sa.Uuid(), nullable=True),
        sa.Column("competitor_run_id", sa.Uuid(), nullable=True),
        sa.Column("penalty", sa.Integer(), nullable=True),
        sa.Column("athlete_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_gates_runs")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "judgement_groups",
        sa.Column("competition_registered_user_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_judgement_groups")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "medal_groups",
        sa.Column("group_name", sa.Text(), nullable=True),
        sa.Column("group_type", sa.Text(), nullable=True),
        sa.Column("competition_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_medal_groups")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "race_classes",
        sa.Column("name", sa.Integer(), nullable=True),
        sa.Column("athletes_qualified_count", sa.Integer(), nullable=True),
        sa.Column("athletes_qualified_percentage", sa.Integer(), nullable=True),
        sa.Column("race_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_race_classes")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "race_registrations",
        sa.Column("race_id", sa.Uuid(), nullable=True),
        sa.Column("competitor_id", sa.Uuid(), nullable=True),
        sa.Column("race_class_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_race_registrations")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "race_stages",
        sa.Column("race_class_id", sa.Uuid(), nullable=True),
        sa.Column("runs_number", sa.Integer(), nullable=True),
        sa.Column("athletes_start_interval", sa.Integer(), nullable=True),
        sa.Column("parent_race_stage_id", sa.Uuid(), nullable=True),
        sa.Column("type", sa.Text(), nullable=True),
        sa.Column("scoring_rule_id", sa.Uuid(), nullable=True),
        sa.Column("athletes_qualified_count", sa.Integer(), nullable=True),
        sa.Column("athletes_qualified_percentage", sa.Integer(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_race_stages")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "races",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("competition_id", sa.Uuid(), nullable=False),
        sa.Column("athletes_start_interval", sa.Integer(), nullable=False),
        sa.Column("scoring_rule_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_races")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "runs",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("race_stage_id", sa.Uuid(), nullable=True),
        sa.Column("scheduled_timestamp", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_runs")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "scoring_rules",
        sa.Column("scoring_rule", sa.Text(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_scoring_rules")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "splits",
        sa.Column("course_element_id", sa.Uuid(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_splits")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "splits_runs",
        sa.Column("split_id", sa.Uuid(), nullable=True),
        sa.Column("competitor_run_id", sa.Uuid(), nullable=True),
        sa.Column("split_time", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_splits_runs")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "starts",
        sa.Column("course_element_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_starts")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "starts_runs",
        sa.Column("start_id", sa.Uuid(), nullable=True),
        sa.Column("competitor_run_id", sa.Uuid(), nullable=True),
        sa.Column("start_time", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_starts_runs")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "user_profiles",
        sa.Column("user_id", sa.Uuid(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_user_profiles")),
        schema="tema_sport_dev",
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        schema="tema_sport_dev",
    )
    op.create_index(
        op.f("ix_tema_sport_dev_users_email"),
        "users",
        ["email"],
        unique=True,
        schema="tema_sport_dev",
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
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["tema_sport_dev.users.id"],
            name=op.f("fk_access_tokens_user_id_users"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("token", "id", name=op.f("pk_access_tokens")),
        schema="tema_sport_dev",
    )
    op.create_index(
        op.f("ix_tema_sport_dev_access_tokens_created_at"),
        "access_tokens",
        ["created_at"],
        unique=False,
        schema="tema_sport_dev",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_tema_sport_dev_access_tokens_created_at"),
        table_name="access_tokens",
        schema="tema_sport_dev",
    )
    op.drop_table("access_tokens", schema="tema_sport_dev")
    op.drop_index(
        op.f("ix_tema_sport_dev_users_email"),
        table_name="users",
        schema="tema_sport_dev",
    )
    op.drop_table("users", schema="tema_sport_dev")
    op.drop_table("user_profiles", schema="tema_sport_dev")
    op.drop_table("starts_runs", schema="tema_sport_dev")
    op.drop_table("starts", schema="tema_sport_dev")
    op.drop_table("splits_runs", schema="tema_sport_dev")
    op.drop_table("splits", schema="tema_sport_dev")
    op.drop_table("scoring_rules", schema="tema_sport_dev")
    op.drop_table("runs", schema="tema_sport_dev")
    op.drop_table("races", schema="tema_sport_dev")
    op.drop_table("race_stages", schema="tema_sport_dev")
    op.drop_table("race_registrations", schema="tema_sport_dev")
    op.drop_table("race_classes", schema="tema_sport_dev")
    op.drop_table("medal_groups", schema="tema_sport_dev")
    op.drop_table("judgement_groups", schema="tema_sport_dev")
    op.drop_table("gates_runs", schema="tema_sport_dev")
    op.drop_table("gates", schema="tema_sport_dev")
    op.drop_table("finishes_runs", schema="tema_sport_dev")
    op.drop_table("finishes", schema="tema_sport_dev")
    op.drop_table("course_elements", schema="tema_sport_dev")
    op.drop_table("competitors_medal_groups", schema="tema_sport_dev")
    op.drop_table("competitors", schema="tema_sport_dev")
    op.drop_table("competitor_runs", schema="tema_sport_dev")
    op.drop_table("competitions", schema="tema_sport_dev")
    op.drop_table("competition_scoring_rules", schema="tema_sport_dev")
    op.drop_table("competition_results", schema="tema_sport_dev")
    op.drop_table("competition_registered_users", schema="tema_sport_dev")
    op.drop_table("competition_owners", schema="tema_sport_dev")
    op.drop_table("bibs_competitiors", schema="tema_sport_dev")
    op.drop_table("bibs", schema="tema_sport_dev")
    op.drop_table("bib_athletes", schema="tema_sport_dev")
    op.drop_table("athletes", schema="tema_sport_dev")
    op.drop_table("agg_run_results", schema="tema_sport_dev")
    op.drop_table("agg_race_results", schema="tema_sport_dev")
    # ### end Alembic commands ###
