from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token='5267120267:AAElS0qicMnvigpgoIFxZfrpk_Pf8cPBOMY')
dp = Dispatcher(bot)

votes = {}


urlkb = InlineKeyboardMarkup(row_width=2)
but1 = InlineKeyboardButton(text='Ссылка', url='https://gb.ru/blog/tipy-dannykh-sql/')
but2 = InlineKeyboardButton(text='Ссылка2', url='https://web.telegram.org/k/#@BotFather')
lst_urls = [InlineKeyboardButton(text='Ссылка3', url='https://web.telegram.org/k/#@BotFather'), InlineKeyboardButton(text='Ссылка4', url='https://web.telegram.org/k/#@BotFather'),
            InlineKeyboardButton(text='Ссылка5', url='https://web.telegram.org/k/#@BotFather')]
urlkb.add(but1, but2).row(*lst_urls).insert(InlineKeyboardButton(text='Ссылка6', url='https://web.telegram.org/k/#@BotFather'))

@dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
    await message.answer('Ссылочки: ', reply_markup=urlkb)

callkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'), InlineKeyboardButton(text='Unlike', callback_data='like_-1') )


@dp.message_handler(commands='test')
async def inline_command(message : types.Message):
    await message.answer('За Россию сучки: ', reply_markup=callkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_test(callback : types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in votes:
        votes[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)
    # await callback.message.answer('Вы нажали на инлайн кнопку!!')
    # await callback.answer('Вы рады', show_alert=True)

executor.start_polling(dp, skip_updates=True)




