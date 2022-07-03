from aiogram import executor

from loader import dp
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api import porn_db, porn_foto

from plyer import notification


def show_niti(title, message):
    notification.notify(title=title,
                        message=message,
                        timeout=3)


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    try:
        porn_db.sql_start()
        show_niti('Porn_db', "Conected")
    except:
        show_niti('Porn_db', "Conected error")

    try:
        porn_foto.sql_start_foto()
        show_niti('Porn_db_foto', "Conected")
    except:
        show_niti('Porn_db_foto', "Conected error")


async def on_shutdown(dispatcher):

    await on_shutdown_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,
                           on_shutdown=on_shutdown)
