from sqlalchemy import (
    Column,
    String,
)
from backend.core.models.base import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "tema_sport"}

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = Column(String, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"


class Competition(Base):
    __tablename__ = "base"
    __table_args__ = {"schema": "tema_sport"}

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = Column(String, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"
