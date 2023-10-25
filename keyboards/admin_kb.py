from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Загрузить')
b2 = KeyboardButton('/Удалить')


button_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(b1).add(b2)
