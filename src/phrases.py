import emoji
from aiogram.utils.markdown import hlink

START_BOT = 'Бот запущен'
STOP_BOT = 'Бот выключен'

link = hlink("команда Bubble Hub", "https://t.me/bubblehubb")
HELLO_TEXT = (f'Здравствуйте,  {link} хочет, чтобы вы тоже стали частью нашей культуры {emoji.emojize(":bubble_tea:")}\nПройдите викторину '
              'и получите приятный приз 🎁')

QUIZ_START_TEXT = 'Да начнётся викторина 🏁'

LAST_STAND = "Простите, я вас не понимаю 🥺"
LAST_STAND_START = "Вы уже стали участником викторины 🥺"

SPAM_ATTACK = (f"Вы участвовали в нашей викторине, и мы решили поблагодарить Вас за то, что  Вы часть нашей культуры! \nДо <b>12.08</b> покажите это сообщение бариста и <b>получите скидку 15%</b> 🎁\n"
               f"\n Приходите к Нам в Bubble Hub {emoji.emojize(':bubble_tea:')}"
               f"\n\n<b>📍 Карла Либкнехта 8Б"
               f"\n🕐 Ежедневно, 10:00 - 22:00</b>")
STOP_QUIZ_THX = 'Спасибо, что остаетесь с нами 🥰'