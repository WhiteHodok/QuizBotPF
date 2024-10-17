from src.db.models import UserInfo, UserRating, Questions
from src.utils.repository import SQLAlchemyRepository

"""
В данном файле описываются модели поведения для fabric репозитория
"""


class UserRepository(SQLAlchemyRepository):
    model = UserInfo


class RatingRepository(SQLAlchemyRepository):
    model = UserRating


class QuestionsRepository(SQLAlchemyRepository):
    model = Questions
