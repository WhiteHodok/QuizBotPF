from datetime import datetime
from pydantic import BaseModel, Field

"""
В данном файле описываются схемы данных(внутри БД) для модуля test_service.py
"""


class User(BaseModel):
    chat_id: str = Field(examples=["TEXT"])
    tg_username: str = Field(examples=["TEST TEXT"])


class Rating(BaseModel):
    chat_id: str = Field(examples=["TEXT"])
    tg_username: str = Field(examples=["TEST TEXT"])
    rating: int = Field(examples=[5])


class Questions(BaseModel):
    num: int = Field(examples=[5])
    question: str = Field(examples=["TEST TEXT"])
    variants: str = Field(examples=["TEST TEXT"])