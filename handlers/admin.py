from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    desc = State()
    price = State()


# Получаем id текущего пользователя
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def makes_change_command(message : types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'What do you want?', reply_markup=admin_kb.button_admin)
    await message.delete()



# start dialog and upload menu
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')


#команда отмены
# @dp.message_handler(state="*", commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handlers(message : types.Message, state : FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return 
    await state.finish()
    await message.reply('OK')


# ловим первый ответ, записываем его в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь введи название')

# ловим второй ответ 
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')

# третий ответ 
# @dp.message_handler(state=FSMAdmin.desc)
async def load_description(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь введи цену')

# четвертый ответ, используем полученные данные
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sqlite_db.sql_add_command(state)
        await state.finish()



# отлавливаем инф. от инлайн-кнопки
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def callback_del(callback_query : types.CallbackQuery):
    name = callback_query.data.split(' ')[1]
    await sqlite_db.sql_del_command(name)
    await callback_query.answer(text = f'{name} удален', show_alert=True)

# инлайн-клавиатура для удаления
# @dp.message_handler(commands='Удалить')
async def delete_item(message : types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read_admin()
        for s in read:
            await bot.send_photo(message.from_user.id, s[0], f'{s[1]}\nОписание: {s[2]}\nЦена: {s[3]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {s[1]}', callback_data=f'del {s[1]}')))



# Регистрация 
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handlers, state="*", commands='отмена')
    dp.register_message_handler(cancel_handlers, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.desc)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(makes_change_command, commands=['moderator'], is_chat_admin=True)
    # dp.register_message_handler(callback_del, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_item, commands='Удалить')






