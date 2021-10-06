import requests
import json


def print_dictionary_values(dict):
    for key in dict:
        print(f'{key} - {dict[key]}')
    print('\n\n\n')


def print_list_values(list):
    for el in list:
        print(f'{el}')


# Сначала выводил список своих репо user_name = "android156" но работает для любого, ниже user_name преподавателя
# по алгоритмам, все также работает
user_name = "DmitryChitalov"
api_user_repos_url = f'https://api.github.com/users/{user_name}/repos'
# Список репозиториев пользователя выдается только авторизованным пользователям, пришлось создать token на
# github и загнать в headers

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
           'Authorization': 'token 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'}
req = requests.get(api_user_repos_url, headers)
user_data = json.loads(req.text)  # тут почему-то возвращается список словарей, выводим все на экран, но в принципе
# можно было дернуть только названия.
print_list_values(user_data)
# Сохраняем список репозиториев в json файл
with open('data.txt', 'w') as outfile:
    json.dump(req.text, outfile)

# В качестве второго API взял погоду, сменил город на Москву, температуру получил в градусах, вывод
# города на русском языке после смены параметра lang, но все остальное английское осталось.
print("\n\nAPI Погода")

appid = '26c993f861d97515014a0533e3281004'
service = 'https://api.openweathermap.org/data/2.5/weather'
language = 'ru'
metric = 'metric'
req = requests.get(f'{service}?q=Moscow&appid={appid}&lang={language}&units={metric}')
data = json.loads(req.text)
print(f'req.text сунули в JSON.loads - {type(data)}')
print_dictionary_values(data)

