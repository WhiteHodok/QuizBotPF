from src.services.test_service import UserService
from src.repo.repositories import UserRepository, UserInfo, UserRating, Questions, RatingRepository, QuestionsRepository

"""
В данном файле описываются и инициализируются сервисы для fabric репозитория
"""


def user_service_fabric():
    return UserService(UserRepository())

def user_rating_fabric():
    return UserService(RatingRepository())

def user_question_fabric():
    return UserService(QuestionsRepository())
