from aiogram.fsm.state import State, StatesGroup


class User_state(StatesGroup):
    quiz = State()
    stop_quiz = State()