from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рандом")
        ],
        [
            KeyboardButton(text="Категории"),
            KeyboardButton(text="Фото")
        ],
    ],
    resize_keyboard=True

)
