from aiogram.types import InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import emoji


def go_quiz_keyboard_maker():
    quiz_builder = InlineKeyboardBuilder()
    quiz_buttons_names = {'go': f'{emoji.emojize(":bubble_tea:")} Пройти викторину'}
    go_quiz_button = InlineKeyboardButton(text=quiz_buttons_names['go'], callback_data="go_quiz")
    quiz_builder.row(go_quiz_button)
    return quiz_builder.as_markup()

def go_media_keyboard_maker():
    media_builder = InlineKeyboardBuilder()
    media_buttons_names = {'media': f'{emoji.emojize(":bubble_tea:")} Перейти в Telegram канал'}
    go_media_button = InlineKeyboardButton(text=media_buttons_names['media'], url='https://t.me/bubblehubb')
    media_builder.row(go_media_button)
    return media_builder.as_markup()
