from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Загрузить_Видео"),
            KeyboardButton(text="Загрузить_Фото")
        ],
    ],
    resize_keyboard=True

)
