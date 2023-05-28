import asyncio
import aiohttp
import json 
import requests
import pandas as pd
import numpy as np
from dop_parser import choose_catalog

# парсер артикула 
def get_data_id(id):
    url = f'https://card.wb.ru/cards/detail?appType=1&curr=rub&dest=-1257786&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&spp=0&nm={id}'

    try:
        response = requests.get(url).text
        data_json = json.loads(response)
        data = data_json['data']['products'][0]
        sum_qty = sum(map(lambda x: x['qty'], data['sizes'][0]['stocks']))
        cards_data = {
            'Наименование': data['name'],
            'Артикул': data['id'],
            'Цена': int(data['priceU'] / 100),
            'Цена со скидкой': int(data["salePriceU"] / 100),
            'Рейтинг' : data['rating'],
            'Остаток на складе' : sum_qty}
        
        return cards_data
    
    except Exception as e:
        print(f'{id}: Ошибка - {e}')




# возвращает готовый словарь со спарсенными данными 
def get_data_from_json(json_file):
    data_list = []
    for data in json_file['data']['products']:
        try:
            price = int(data["priceU"] / 100)
        except:
            price = 0
        data_list.append({
            'Наименование': data['name'],
            'Артикул': data['id'],
            'Цена': price,
            'Цена со скидкой': int(data["salePriceU"] / 100)
        })
    return data_list

# главная функция вызывает оставщиеся
def get_content(shard, query,count=10, low_price=0, top_price=0):
    headers = {'Accept': "*/*", 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    data_list = []
    for page in range(1, count):
        print(f'Сбор позиций со страницы {page} из 100')
        url = f'''https://catalog.wb.ru/catalog/{shard}/catalog?appType=1&{query}&curr=rub&dest=-1257786&page={page}&priceU={low_price * 100};{top_price * 100}&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&sort=popular&spp=0'''
        r = requests.get(url, headers=headers)
        data = r.json()
        print(f'Добавлено позиций: {len(get_data_from_json(data))}')
        if len(get_data_from_json(data)) > 0:
            data_list.extend(get_data_from_json(data))
        else:
            print(f'Сбор данных завершен.')
            break
    return data_list

# try:
#     shard, query = choose_catalog(input('Введите нужный вам каталог: '))
#     print(shard, query)
# except Exception as e:
#     print(f'{e} каталог не найден')

# count, low, top = int(input('Введите число страниц до 100: ')), int(input('Введите нижнию цену: ')), int(input('Введите верхнию цену: '))

# print(get_content(shard, query,count, low, top))






