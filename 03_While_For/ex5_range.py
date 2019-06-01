# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //     Функция range(), которая возвращает итератор
# //

HEADLINE: str = ' Функция range(), которая возвращает итератор  '

print('\n')
print(HEADLINE.center(80, '*'), '\n')

a = list(range(5))
print(a)

a = list(range(2, 5))
print(a)

del a[1]
print(a)

a = list(range(-5, 5))
print(a)

a = list(range(5, -5, -1))
print(a)

a = list(range(-5, 5, 2))
print(a)

for i in range(10):
    print(i, 'привет!')
