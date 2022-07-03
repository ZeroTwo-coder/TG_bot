from aiogram.dispatcher.filters.state import StatesGroup, State


class Video(StatesGroup):
    photo = State()
    title = State()
    decription = State()
    video = State()
