from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import hashlib

from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

bot = Bot(token='5739490991:AAFjXNnLgpCyk91pfodjgAFdV-yEtgVD8iA')
dp = Dispatcher(bot)


@dp.message_handler()
async def start(message : types.Message):
    await message.answer('Я инлайн-бот, не нужно мне писать')

@dp.inline_handler()
async def inline_handler(query : types.InlineQuery):
    text = query.query or 'echo'
    link = 'https://ru.wikipedia.org/wiki/' + text
    result_id:str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id = result_id,
        title='Статья из Wiki', 
        url=link,
        input_message_content=types.InputTextMessageContent(
            message_text=link))]
    
    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp, skip_updates=True)