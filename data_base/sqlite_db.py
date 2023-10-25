import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('pizza.db')
    cur = base.cursor()
    if base:
        print('DataBase connected OK')
    base.execute('create table if not exists menu(img text, name text primary key,  desc text, price decimal(10.2))')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('insert into menu values (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for s in cur.execute('select * from menu').fetchall():
        await bot.send_photo(message.from_user.id, s[0], f'{s[1]}\nОписание: {s[2]}\nЦена: {s[3]}')

async def sql_read_admin():
    return cur.execute('select * from menu').fetchall()


async def sql_del_command(data):
    cur.execute('DELETE FROM menu WHERE name = ?', (data,))
    base.commit()


