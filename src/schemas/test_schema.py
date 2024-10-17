from datetime import datetime
from pydantic import BaseModel, Field

"""
В данном файле описываются схемы данных(внутри БД) для модуля test_service.py
"""


class UserCreate(BaseModel):
    chat_id: int = Field(examples=[5])
    text: str = Field(examples=["Отличное приложение!"])


class User(BaseModel):
    chat_id: int = Field(examples=[5])
    tg_username: str = Field(examples=["TEST TEXT"])


class Rating(BaseModel):
    chat_id: int = Field(examples=[5])
    tg_username: str = Field(examples=["TEST TEXT"])
    rating: int = Field(examples=[5])
