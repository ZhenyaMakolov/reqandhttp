import requests

from pprint import pprint

super_heroes = ['Hulk', 'Captain America', 'Thanos']

def identifying_smarted(super_heroes):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url)
    list_heroes = super_heroes
    heroes = {}
    value_intelligence = []
    for i in response.json():
        if i.get('name') in list_heroes:
            heroes[i['name']] = i['powerstats']['intelligence']
    for number in heroes.values():
        value_intelligence.append(int(number))
    for key, value in heroes.items():
        if value == max(value_intelligence):
            res = (f'Самый умный герой: {key} с количеством интеллекта {value}')
    return print(res)

if __name__ == '__main__':
    identifying_smarted(super_heroes)