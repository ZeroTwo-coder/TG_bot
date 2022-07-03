import sqlite3 as sq
import random

from loader import bot


def sql_start():
    global base, cur
    base = sq.connect('porn_db')
    cur = base.cursor()
    if base:
        print('Data base connect good!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS porn(photo TEXT, title TEXT, decription TEXT, url TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        try:
            cur.execute('INSERT INTO porn VALUES(?,?,?,?)',
                        tuple(data.values()))
        except Exception as e:
            print(e)
        base.commit()


async def sql_read(message):
    item = cur.execute('SELECT * FROM porn').fetchall()
    long_arr = random.randint(0, len(item) - 1)
    await bot.send_photo(message.from_user.id, item[long_arr][0], f'"{item[long_arr][1]}"\n\n{item[long_arr][2]}')
    await bot.send_video(message.from_user.id, item[long_arr][3])
