from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .database import Base
from sqlalchemy import TIMESTAMP, BigInteger, Column, Sequence, String, text, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Column,
    Sequence,
    String,
    text,
    Integer,
    Index,
)
from .database import Base


class Result(Base):
    __tablename__ = "results"
    __table_args__ = {"schema": "public"}

    id = Column(
        BigInteger,
        server_default=Sequence(
            f"{__tablename__}_id_seq", schema=__table_args__["schema"]
        ).next_value(),
    )
    # id = Column(Integer, primary_key=True, index=True,
    #             server_default=Sequence( f"{__tablename__}_id_seq"  ).next_value())
    participant_id = Column(
        Integer,
        index=True,
        primary_key=True,
    )
    start_time = Column(Integer, nullable=True)
    finish_time = Column(Integer, nullable=True)
    total_time = Column(Integer, nullable=True)
    penalties = Column(Integer, default=0)
    race_id = Column(
        Integer,
        index=True,
        primary_key=True,
    )

    __table_args__ = (
        Index("idx_unique_race_participant", "race_id", "participant_id", unique=True),
    )
