from aiogram.fsm.state import StatesGroup, State


class ChatMode(StatesGroup):
    GET_MESSAGE = State()
