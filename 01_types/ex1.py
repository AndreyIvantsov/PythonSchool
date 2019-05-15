# -*- coding: utf-8 -*-

# /////////////////////////////////
# // Форматирование чисел
# //

from random import uniform


a = 234.345
b = 2.4
c = 0.123456789

for m in [a, b, c]:
    print("%10.4f" % m)

print('-' * 45)

rnd_list = []

for i in range(10):
    rnd_list.append(uniform(-1000.0, 1000.0))

nom = 1

word_list = ['Первый', 'Красный', 'Зеленый', 'Второй', 'Санкт-Петербург',
             'Тверь', 'Рзовый', 'Переизбыточный', 'Явь', 'Третий']

for rnd_number in rnd_list:
    print('{0:0>3d} : {1:10.4f}'.format(nom, rnd_number))
    nom += 1

print('-' * 70)

for rnd_number, word in zip(rnd_list, word_list):
    print('{0:0>3d} : {1:10.4f} : {2:20} : {3:>20}'.format(nom, rnd_number, word, word))
    nom += 1



