import sqlite3 as sq
import random

from loader import bot


def sql_start_foto():
    global base, cur
    base = sq.connect('porn_db_foto')
    cur = base.cursor()
    if base:
        print('Data base connect good!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS porn_foto(photo TEXT)')
    base.commit()


async def sql_add_command_foto(state):
    async with state.proxy() as data:
        try:
            cur.execute('INSERT INTO porn_foto VALUES(?)',
                        tuple(data.values()))
        except Exception as e:
            print(e)
        base.commit()


async def sql_read_foto(message):
    item = cur.execute('SELECT * FROM porn_foto').fetchall()
    long_arr = random.randint(0, len(item) - 1)
    await bot.send_photo(message.from_user.id, item[long_arr][0])
