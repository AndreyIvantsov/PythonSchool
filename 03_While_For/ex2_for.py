# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //                      Цикл for
# //

HEADLINE: str = ' Цикл for '

print('\n')
print(HEADLINE.center(40, '*'), '\n')


# Обход строки

word = input('Введете строку: ')

for letter in word:
    print("{}.".format(letter), end='')

print('\n')

# Функция range()

for i in range(10):
    print(i, end=' ')

print('\n')

for i in range(5, 10):
    print(i, end=' ')

print('\n')

for i in range(20, 10, -1):
    print(i, end=' ')

print('\n')

for i in range(5, 30, 3):
    print(i, end=' ')

print('\n')

# Обход кортежа

colors = ('red', 'yellow', 'green',)  # Кортеж

for color in colors:
    print(color)

print('\n')

#  Выборка одинаковых элементов

lst_1 = ['Sem', 'Jon', 235, ('3', 3), 3.14, 555, 'Red']

lst_2 = [777, 'Sem',  ('3', 3), 3.14,  'Green', 'Jon']

selection = []

for item in lst_1:
    if item in lst_2:
        selection.append(item)

print('Первый список       :', lst_1)
print('Второй список       :', lst_2)
print('Одинаковые эметенты :', selection)

