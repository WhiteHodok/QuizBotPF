import asyncio
from aiogram import Router
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from config import bot, bot_settings
from src.keyboards.user_inline_keyboards import go_quiz_keyboard_maker, go_media_keyboard_maker
from src.phrases import HELLO_TEXT, LAST_STAND_START, SPAM_ATTACK, STOP_QUIZ_THX
from src.states.user_state import User_state
from src.db.models import Questions, UserInfo, UserRating
from src.utils.dependencies.user_service import user_service_fabric, user_rating_fabric, user_question_fabric
from src.schemas.test_schema import User, Rating, Questions

user_router = Router()
response = user_service_fabric()
user_rating_response = user_rating_fabric()
question_response = user_question_fabric()


@user_router.message(CommandStart(), StateFilter(None))
async def command_start(message: Message, state: FSMContext) -> None:
        tg_username = message.chat.username
        chat_id = message.from_user.id
        insert_id = str(chat_id)
        user_data = await response.user_get_all_users([UserInfo.chat_id == insert_id])
        if not user_data:
            await response.user_insert({
                "chat_id": insert_id,
                "tg_username": tg_username})
        else:
            try:
                user_rating_response.rating_delete([Rating.chat_id == insert_id])
            except:
                pass
        await bot.send_message(
            chat_id=chat_id,
            text=HELLO_TEXT,
            reply_markup=go_quiz_keyboard_maker(),
            parse_mode='HTML',
            disable_web_page_preview=True
        )
        await state.set_state(User_state.quiz)



@user_router.message(StateFilter(User_state.stop_quiz))
async def in_stop_quiz(message: Message, state: FSMContext) -> None:
    await message.answer(STOP_QUIZ_THX)


@user_router.message(CommandStart())
async def command_start_in_quiz(message: Message, state: FSMContext) -> None:
    await message.answer(LAST_STAND_START)


@user_router.message(Command('spam_attack'))
async def spam_attack(message: Message, state: FSMContext) -> None:
    chat_id = message.chat.id
    if bot_settings.ADMIN_ID == chat_id:
        user_data = await response.user_get_all_users()
        counter = 0
        list_len = len(user_data)
        for user in user_data:

                counter += 1
                await asyncio.sleep(0.5)
                file_path = './src/handlers/cords2.jpg'
                await bot.send_photo(
                    chat_id=user['chat_id'],
                    caption=SPAM_ATTACK,
                    parse_mode="HTML",
                    reply_markup=go_media_keyboard_maker(),
                    photo=FSInputFile(file_path)
                )
                await state.set_state(User_state.stop_quiz)
                await bot.send_message(chat_id=chat_id,
                                       text=f"({counter}/{list_len}) {user['chat_id']} - сообщение успешно отправлено")
        await bot.send_message(chat_id=chat_id, text='Спам атака завершена')
