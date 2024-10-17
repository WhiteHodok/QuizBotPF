import asyncio

from aiogram import Router
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from config import bot, supabase, secrets
from src.handlers.events import error_bot
from src.keyboards.user_inline_keyboards import go_quiz_keyboard_maker, go_media_keyboard_maker
from src.phrases import HELLO_TEXT, LAST_STAND_START, SPAM_ATTACK, STOP_QUIZ_THX
from src.states.user_state import User_state

user_router = Router()


@user_router.message(CommandStart(), StateFilter(None))
async def command_start(message: Message, state: FSMContext) -> None:
    try:
        tg_username = message.chat.username
        chat_id = message.from_user.id
        user_data = supabase.from_("UserData").select("*").eq(
            "chat_id", chat_id
        ).execute()
        if not user_data.data:
            supabase.table("UserData").insert({
                "chat_id": chat_id,
                "tg_username": tg_username
            }).execute()
        else:
            try:
                supabase.table("Rating").delete().eq("chat_id", chat_id).execute()
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
    except Exception as e:
        await error_bot('command start', message, str(e))

@user_router.message(StateFilter(User_state.stop_quiz))
async def in_stop_quiz(message: Message, state: FSMContext) -> None:
    await message.answer(STOP_QUIZ_THX)

@user_router.message(CommandStart())
async def command_start_in_quiz(message: Message, state: FSMContext) -> None:
    await message.answer(LAST_STAND_START)


@user_router.message(Command('spam_attack'))
async def spam_attack(message: Message, state: FSMContext) -> None:
    chat_id = message.chat.id
    if secrets.admin_id == chat_id:
        user_data = supabase.from_("UserData").select("*").execute()
        counter = 0
        list_len = len(user_data.data)
        for user in user_data.data:
            try:
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
                await bot.send_message(chat_id=chat_id, text=f"({counter}/{list_len}) {user['chat_id']} - сообщение успешно отправлено")
            except Exception as e:
                await bot.send_message(chat_id=chat_id, text=f"({counter}/{list_len}) {user['chat_id']} - {e}")
        await bot.send_message(chat_id=chat_id, text='Спам атака завершена')




