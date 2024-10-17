from src.repo.repositories import UserRepository
from src.schemas.test_schema import User, Rating, Questions
from src.utils.repository import AbstractRepository

"""
В данном файле описываются и инициализируются сервисы для fabric репозитория
"""


class UserService:


    def __init__(self, repo: AbstractRepository):
        self.repo = repo

    async def user_insert(self, data: User):
        await self.repo.add_one(data)

    async def rating_insert(self, data: Rating):
        await self.repo.add_one(data)

    async def question_insert(self, data: Questions):
        await self.repo.add_one(data)

    async def user_get(self, data: User):
        return await self.repo.get_one(data)

    async def rating_get(self, data: Rating):
        return await self.repo.get_one(data)

    async def question_get(self, data: Questions):
        return await self.repo.get_one(data)

    async def rating_update(self, data: Rating):
        await self.repo.update_one(data)

    async def user_update(self, data: User):
        await self.repo.update_one(data)

    async def question_update(self, data: Questions):
        await self.repo.update_one(data)

    async def user_delete(self, data: User):
        await self.repo.delete_one(data)

    async def rating_delete(self, data: Rating):
        await self.repo.delete_one(data)

    async def question_delete(self, data: Questions):
        await self.repo.delete_one(data)

    async def user_get_all_users(self, data: User):
        return await self.repo.get_all_by_filter(data)

    async def rating_get_all_users(self, data: Rating):
        return await self.repo.get_all_by_filter(data)

    async def question_get_all_users(self, data: Questions):
        return await self.repo.get_all_by_filter(data)


