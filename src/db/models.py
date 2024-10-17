from typing import (
    List,
    Optional
)
from sqlalchemy.orm import (
    relationship,
    Mapped,
    mapped_column,
)
from sqlalchemy import (
    Boolean,
    Column,
    Float,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from datetime import datetime
from src.db.conn import Base


class User(Base):
    __tablename__ = "test"

    chat_id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))


class UserInfo(Base):
    __tablename__ = "UserData"

    chat_id: Mapped[int] = mapped_column(primary_key=True)
    tg_username: Mapped[str] = mapped_column(String(255))


class UserRating(Base):
    __tablename__ = "Rating"

    chat_id: Mapped[int] = mapped_column(primary_key=True)
    tg_username: Mapped[str] = mapped_column(String(255))
    rating: Mapped[int] = mapped_column(Integer)

#TODO FOR QUESTIONS