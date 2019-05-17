# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //                    Словари
# //

""" ********************************************************
# Словарь - изменяемый, не упорядоченный объек

переменная = {'ключ1': значение1, 'ключ2': значение2}
переменная = dict('ключ1': значение1, 'ключ2': значение2)

    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    a == b == c == d == e

******************************************************** """

animals_dict = {'cat': 'кошка', 'dog': 'собака', 'mouse': 'мышка'}

print(animals_dict)

print(animals_dict['cat'])
print(animals_dict['dog'])
print(animals_dict['mouse'], '\n')


dishes_dict = dict(plate='тарелка', cup='чашка', spoon='ложка')

print(dishes_dict, '\n')

print('{0:*<25}|{1:-^25}|{2:+>25}'.format(dishes_dict['plate'], dishes_dict['cup'], dishes_dict['spoon']), '\n')

# Основные методы словарей

house = {'roof': 'крыша', 'window': 'окна', 'walls': 'стены'}

print(house, '\n')
print(len(house))

print(house.keys())         # выводит список ключей
print(house.values())       # выводит список значений
print(house.items(), '\n')  # выводит список ключей и значений

print(list(house.keys()))
print(list(house.values()))
print(list(house.items()), '\n')

# Добавление, удаление, изменение элементов словарей

house['roof'] = 'навес'     # изменение
print(house, '\n')

del house['walls']          # удаление
print(house, '\n')

house['door'] = 'дверь'     # добавление нового
print(house, '\n')

# Заполнение словаря

example = {
    'name': 'Василий',
    'web': ['pro365.ru', 'pro365.net'],
    'adr': {'city': 'Мурманск', 'street': 'Ленина'},
    'nom': 3
}

print(example, '\n')

print(example['name'])
print(example['web'][0])
print(example['web'][1])
print(example['adr']['city'])
print(example['adr']['street'])
print(example['nom'])











