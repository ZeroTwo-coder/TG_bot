from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from loader import dp
from data.config import is_admin
from keyboards.default import kb_admin, kb_start
from states import Video, Photo
from utils.db_api import porn_db, porn_foto


@dp.message_handler(Command('load'))
async def bot_load(message: types.Message):
    global admin_tocken
    for admin in is_admin:
        if admin == message.from_user.id:
            admin_tocken = True
            break
        else:
            admin_tocken = False

    if admin_tocken:
        await message.answer("Проходи, ты вроде админ", reply_markup=kb_admin)
    else:
        await message.answer("Иш что удумал, ты не админ!")


@dp.message_handler(Text(equals=['Загрузить_Видео']))
async def bot_load_video(message: types.Message, state=None):
    global admin_tocken
    for admin in is_admin:
        if admin == message.from_user.id:
            admin_tocken = True
            break
        else:
            admin_tocken = False

    if admin_tocken:
        await message.answer("Проходи, ты вроде админ", reply_markup=ReplyKeyboardRemove())
        await Video.photo.set()
        await message.answer('Загрузи фото')
    else:
        await message.answer("Иш что удумал, ты не админ!")


@dp.message_handler(Text(equals=["Загрузить_Фото"]))
async def bot_load_photo(message: types.Message, state=None):
    global admin_tocken
    for admin in is_admin:
        if admin == message.from_user.id:
            admin_tocken = True
            break
        else:
            admin_tocken = False

    if admin_tocken:
        await message.answer("Проходи, ты вроде админ", reply_markup=ReplyKeyboardRemove())
        await Photo.photo.set()
        await message.answer('Загрузи фото')
    else:
        await message.answer("Иш что удумал, ты не админ!")


@dp.message_handler(content_types=['photo'], state=Photo.photo)
async def load_foto(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await porn_foto.sql_add_command_foto(state)
    await state.finish()
    await message.answer("Это успех", reply_markup=kb_start)


@dp.message_handler(content_types=['photo'], state=Video.photo)
async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await Video.next()
    await message.answer("Теперь ввидите название")


@dp.message_handler(state=Video.title)
async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await Video.next()
    await message.answer("Теперь ввидите описание")


@dp.message_handler(state=Video.decription)
async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['decription'] = message.text
    await Video.next()
    await message.answer("Скиньте видео")


@dp.message_handler(content_types=['video'], state=Video.video)
async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['video'] = message.video.file_id
    await porn_db.sql_add_command(state)
    await state.finish()
    await message.answer("Успешно загруженно", reply_markup=kb_start)
