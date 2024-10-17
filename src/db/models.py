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


class UserInfo(Base):
    __tablename__ = "UserData"

    chat_id: Mapped[str] = mapped_column(primary_key=True)
    tg_username: Mapped[str] = mapped_column(String(255), nullable=True)


class UserRating(Base):
    __tablename__ = "Rating"

    chat_id: Mapped[str] = mapped_column(primary_key=True)
    tg_username: Mapped[str] = mapped_column(String(255), nullable=True)
    rating: Mapped[int] = mapped_column(Integer, nullable=True)

class Questions(Base):
    __tablename__ = "Questions"

    num: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(1024))
    variants: Mapped[str] = mapped_column(String(1024))

