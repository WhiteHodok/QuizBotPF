import asyncio
import logging
import sys
from aiogram import F
from aiogram.fsm.scene import SceneRegistry
from aiogram.methods import DeleteWebhook
from config import dp, bot
from src.handlers.quiz_scene import QuizScene
from src.handlers.user_handler import user_router
from src.utils.dependencies.user_service import user_service_fabric
import asyncio


async def start():
    dp.include_router(user_router)
    user_router.callback_query.register(QuizScene.as_handler(), F.data == 'go_quiz')
    scene_registry = SceneRegistry(dp)
    scene_registry.add(QuizScene)

    try:
        await bot(DeleteWebhook(drop_pending_updates=True))
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())
