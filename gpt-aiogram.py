# -*- coding: utf-8 -*- 

from aiogram import Bot, Dispatcher, executor, types
import openai


bot = Bot('6064761154:AAHpetSzNO5SEqNGfrZbph7vBErsWPn9TFQ')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет!\nЯ GPT3 бот \nОтправь мне любое сообщение, начинающееся с !, а я тебе обязательно отвечу")


@dp.message_handler()
async def echo(message: types.Message):
    if message.text[0] == "!":
        openai.api_key = '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'
        completion = openai.Completion.create(model="text-davinci-003",
                                              prompt=message.text[1::],
                                              temperature=0.7,
                                              max_tokens=2048,
                                              top_p=1.0,    
                                              frequency_penalty=0,
                                              presence_penalty=0.0)
        await message.answer(completion.choices[0].text)



# Как сделать чтобы она по частям отсылылы сгенерированный текст 
# @dp.message_handler()
# async def echo(message: types.Message):
#     if message.text[0] == "!":
#         openai.api_key = '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'
#         prompt = message.text[1::]
#         temperature = 0.7
#         max_tokens = 2048
#         top_p = 1.0
#         frequency_penalty = 0
#         presence_penalty = 0.0
        
#         async with openai.GPT(model="text-davinci-003", api_key=openai.api_key) as gpt:
#             async for result in gpt.stream(prompt=prompt,
#                                            temperature=temperature,
#                                            max_tokens=max_tokens,
#                                            top_p=top_p,
#                                            frequency_penalty=frequency_penalty,
#                                            presence_penalty=presence_penalty):
#                 text = result['text']
#                 await message.answer(text)



# КАК ПРИМЕР РАБОТАЕТ ВРОДЕ АНАЛОГИЧНО ПЕРВОМУ
# @dp.message_handler()
# async def echo(message: types.Message):
#     if message.text[0] == "!":
#         openai.api_key = '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'
#         completion = openai.Completion.create(model="text-davinci-003",
#                                               prompt=message.text[1::],
#                                               temperature=0.7,
#                                               max_tokens=2048,
#                                               top_p=1.0,
#                                               frequency_penalty=0,
#                                               presence_penalty=0.0)
#         await bot.send_message(message.chat.id, completion.choices[0].text)



executor.start_polling(dp, skip_updates=True)




# Представь, что ты помощник для первого курса РКСИ.Ростовский колледж связи и информатики (РКСИ) - это среднее профессиональное образовательное учреждение, которое находится в городе Ростов-на-Дону. Тебя зовут Рукси. Твоя задача рассказать о колледже и помочь освоиться студентам. Избегай любых тем, не связанных с жизнью колледжа.Старайся быть дружелюбным и приветливым. Говори студенту, что за более полной информацией он должен прописать уточняющий вопрос.
#                                                         Ты можешь пользоваться предоставленной информацией:
#                                                         Активности колледжа включают в себя:
#                                                         Штаб студенческий отрядов. Вступив в который студент может работать вожатым, строителем, сервисником, проводником.
#                                                         Волонтерская деятельность. Волонтеры участвую не только в мерояприятиях проводимых в колледже, но и в городских. Также за активную работу закрываются часы летней практики. По всем вопросами обращаться в 219 каб. 1-го корпуса или в 19 кабинет 2-го корпуса.
#                                                         Спортивные секции. В колледже реализованы секции по мини-футболу, волейболу, шахматам, стрельбе, настольному теннису и т.д. Обратиться студент может к Алексею Валентиновичу Гузову, заведующему спортивными секциями  в каб. 125, возле спортивного зала.
#                                                         Творческий кружок. В актовом зале студент может стать участником мероприятий. Вы сможете реализовать себя как танцора, певца, чтеца, оратора и т.п.
#                                                         Также в колледже проходят всевозможные конференции по общеобразовательным дисциплинам, олимпиады, хакатоны*, где студент может продемонстрировать свои знания и навыки в данной отрасли. 
#                                                         Правила внутреннего порядка:
#                                                         В колледже запрещено курение, кроме специально отведенных мест (рядом с магазином "Фасоль" и за углом 1-го корпуса РКСИ).
#                                                         В летний период запрещено  носить шорты и сильно открытую одежду.
#                                                         Обязательное ношение сменной обуви с 15 октября до 15 апреля.