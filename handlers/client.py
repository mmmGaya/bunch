from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_strat(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Whatever you want', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Please, send me a message')

async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Время работы с 9:00 до 21:00')

async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Цирюльника 123', reply_markup=ReplyKeyboardRemove())

# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_strat, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
