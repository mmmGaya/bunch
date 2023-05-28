# пасрер составляющих ссылки для парсинга всего каталога
import requests
import json
import pandas as pd
import numpy as np



def get_catalogs_wb():
    url = 'https://www.wildberries.ru/webapi/menu/main-menu-ru-ru.json'
    headers = {'Accept': "*/*", 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    data = response.json()
    data_list = []
    for d in data:
        try:
            for child in d['childs']:
                try:
                    category_name = child['name']
                    category_url = child['url']
                    shard = child['shard']
                    query = child['query']
                    data_list.append({
                        'category_name': category_name,
                        'category_url': category_url,
                        'shard': shard,
                        'query': query})
                except:
                    continue
                try:
                    for sub_child in child['childs']:
                        category_name = sub_child['name']
                        category_url = sub_child['url']
                        shard = sub_child['shard']
                        query = sub_child['query']
                        data_list.append({
                            'category_name': category_name.lower(),
                            'category_url': category_url,
                            'shard': shard,
                            'query': query})
                except:
                    continue
        except:
            continue
    return data_list # мб заносить не в лист, а в словарь чтобы каждый раз не вызывать функцию 

   

def choose_catalog(name_catalog):
    data_list = get_catalogs_wb()
    for i in range(len(data_list)):
        if data_list[i]['category_name'] == name_catalog.lower():
            return data_list[i]['shard'], data_list[i]['query']
    return 'Не найден'

