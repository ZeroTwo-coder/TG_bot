from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from utils.db_api import porn_db, porn_foto


@dp.message_handler(Text(equals=['Рандом']))
async def bot_random_video(message: types.Message):
    await porn_db.sql_read(message)


@dp.message_handler(Text(equals=['Фото']))
async def bot_random_photo(message: types.Message):
    await porn_foto.sql_read_foto(message)
