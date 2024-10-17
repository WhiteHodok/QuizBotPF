from typing import Any
import random
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.scene import Scene, on
from aiogram.types import Message, PollAnswer, CallbackQuery, FSInputFile
from config import bot
from src.handlers.events import error_bot
from src.handlers.user_handler import command_start
from src.keyboards.user_inline_keyboards import go_media_keyboard_maker
from src.phrases import QUIZ_START_TEXT, LAST_STAND


def search_correct_answer(answer_list: list, correct_answer: str) -> int:
    for i, answer in enumerate(answer_list):
        # Если элемент массива совпадает с заданным элементом
        if correct_answer == answer:
            # Возвращаем номер элемента
            return i


class QuizScene(Scene, state="quiz"):
    @on.callback_query.enter()
    @on.poll_answer.enter()
    async def on_enter(self, event_data: CallbackQuery | PollAnswer, state: FSMContext, step: int | None = 1,
                       correct_answer_count: int | None = 0) -> Any:
        try:
            chat_id = event_data.from_user.id if isinstance(event_data, CallbackQuery) else event_data.user.id
            if step == 1:
                # This is the first step, so we should greet the user
                await bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=event_data.message.message_id,
                    text=QUIZ_START_TEXT,
                    reply_markup=None)
#TODO
            question_info = supabase.from_("Questions").select("*").eq(
                "num", step
            ).execute()
            question_data = question_info.data

            if question_data:
                answer_list = question_data[0]['variants']
                correct_answer = answer_list[0]
                random.seed()
                random.shuffle(answer_list)
                num_correct_answer = search_correct_answer(answer_list, correct_answer)

                await state.update_data(step=step)
                await state.update_data(correct_answer_count=correct_answer_count)
                await state.update_data(answer_list=answer_list)

                await bot.send_poll(
                    chat_id=chat_id,
                    question=f"\[{step}/20] {question_data[0]['question']}",
                    options=answer_list,
                    type="quiz",
                    correct_option_id=num_correct_answer,
                    is_anonymous=False,
                )

            else:
                #TODO
                supabase.table("Rating").insert({
                    "chat_id": chat_id,
                    "tg_username": event_data.user.username,
                    "rating": correct_answer_count
                }).execute()

                user_rating = correct_answer_count
                #TODO
                all_results = supabase.table("Rating").select("rating").execute()
                total_users = len(all_results.data)

                # Подсчет позиции пользователя
                position = sum(1 for result in all_results.data if result['rating'] > user_rating) + 1

                result = (f"Поздравляем, Вы прошли тест! 🥳\n"
                          f"Только сегодня! Покажите это сообщение бариста и получите <b>скидку 20% на напиток</b>\n\n<b>📍 Карла Либкнехта 8Б\n🕐 Ежедневно, 10:00 - 22:00</b>\n"
                          f"\n<b>Ваш результат:</b>\n"
                          f"✅ Верно – {user_rating}\n"
                          f"❌ Неверно – {20 - user_rating}\n"
                          f"🏆{position} место из {total_users} ")

                file_path = './src/handlers/cords.jpg'
                await bot.send_photo(
                    chat_id=chat_id,
                    caption=result,
                    parse_mode="HTML",
                    reply_markup=go_media_keyboard_maker(),
                    photo=FSInputFile(file_path)
                )
                await state.set_data({})
        except Exception as e:
            await error_bot('on enter', event_data, str(e))

    @on.poll_answer()
    async def answer(self, poll_answer: PollAnswer, state: FSMContext) -> None:
        try:
            data = await state.get_data()
            step = data["step"]
            answer_list = data["answer_list"]
            correct_answer_count = data["correct_answer_count"]
            #TODO
            question_info = supabase.from_("Questions").select("variants").eq(
                "num", step
            ).execute()
            question_data = question_info.data

            answer = answer_list[poll_answer.option_ids[0]]
            if answer == question_data[0]['variants'][0]:
                return await self.wizard.retake(step=step + 1, correct_answer_count=correct_answer_count + 1)
            else:
                await self.wizard.retake(step=step + 1, correct_answer_count=correct_answer_count)
        except Exception as e:
            await error_bot('answer', poll_answer, str(e))
            
    @on.message(Command('bug_help'))
    async def bug_help(self, message: Message, state: FSMContext) -> None:
        await state.clear()
        await message.answer('Бот перезагружен')
        #TODO
        supabase.table("Rating").delete().eq("chat_id", message.chat.id).execute()
        await command_start(message, state)
        
    @on.message()
    async def unknown_message(self, message: Message) -> None:
        try:
            await message.answer(LAST_STAND)
        except Exception as e:
            await error_bot('unknown message', message, str(e))

    
