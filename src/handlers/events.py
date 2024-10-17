from aiogram.types import Message
from config import bot, bot_settings
from src.phrases import START_BOT, STOP_BOT


async def start_bot() -> None:
    await bot.send_message(bot_settings.ADMIN_ID, START_BOT)


async def stop_bot() -> None:
    await bot.send_message(bot_settings.ADMIN_ID, STOP_BOT)


async def error_bot(def_name: str, message, error: str) -> None:
    await bot.send_message(
        chat_id=bot_settings.ADMIN_ID,
        text=f'Ошибка в функции <b>{def_name}</b>: \n<code>{error}</code>',
        parse_mode='HTML'
    )

    message_data = str(message)
    parts = [message_data[i:i + 4096] for i in range(0, len(message_data), 4096)]

    # Отправляем части сообщения последовательно
    for part in parts:
        await bot.send_message(
            chat_id=bot_settings.ADMIN_ID,
            text=f'```{part}```'
        )
