# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# // Функция zip(), объединяет два списка попарно в картежи
# //

from typing import Dict, Any

HEADLINE: str = ' Функция zip(), объединяет два списка попарно в картежи  '

print('\n')
print(HEADLINE.center(80, '*'), '\n')

login = ['login1', 'login2', 'login3', 'login4']
password = ['password1', 'password2', 'password3']

# в python3 перед использованием zip() необходимо вызвать
# list(), в отличии от python2

a = list(zip(login, password))

print(a)

# применение for к zip()

images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']

print('\n')

for (x, y, z) in zip(login, password, images):
    print(x, y, z)

# применение for к zip()

a = [1, 2, 3]
b = [4, 5, 6]

print('\n')

for (x, y) in zip(a, b):
    assert isinstance(y, object)
    print(x, '+', y, '=', x + y)

# создание словаря при помощи цикла for

d = {'1': 'moon', '2': 'satellite', '3': 'earth'}

print('\n')

print(d)

keys = ['1', '2', '3']
values = ['moon', 'satellite', 'earth']

d1 = list(zip(keys, values))

print(d1)

d2: Dict[Any, Any] = {}

# преобразуем список картежей в словарь

for (k, v) in d1:
    d2[k] = v

print(d2)



