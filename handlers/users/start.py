from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default import kb_start


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    await message.delete()
    await message.answer(f"Привет, {message.from_user.full_name}!\nЯ именно то что ты искал.😏😱\n   -- Видео\n   -- Фото", reply_markup=kb_start)
