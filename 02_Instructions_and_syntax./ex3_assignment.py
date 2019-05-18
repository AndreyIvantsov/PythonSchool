# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //               Присваивание - Assignment
# //

HEADLINE: str = ' ПРИСВАИВАНИЕ '

print('\n')
print(HEADLINE.center(40, '*'), '\n')

a = 100
b = 'String '
c = [1, 2, 3, 4]
print(a, b, c, '\n')

a, b, c = 200, 'Literal', [5, 6, 7, 8]
print(a, b, c, '\n')

(a, b, c) = 'BOX'
print('a = {}, b = {}, c = {}'.format(a, b, c), '\n')

# Распаковывание последовательносте (только Python3)

(a, *b) = 'BOX'
print('a = {}, b = {}'.format(a, b), '\n')

(*a, b) = 'BOX'
print('a = {}, b = {}'.format(a, b), '\n')

(a, b, c, *d) = [1, 2, 3, 4, 5, 6, 7, 8]
print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d), '\n')

(a, b, *c, d) = [1, 2, 3, 4, 5, 6, 7, 8]
print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d), '\n')

(a, *b, c, d) = [1, 2, 3, 4, 5, 6, 7, 8]
print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d), '\n')

(*a, b, c, d) = [1, 2, 3, 4, 5, 6, 7, 8]
print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d), '\n')

# Групповое присваивание одного значения

a = 'Snow'
b = a
c = b
print('a = {}, b = {}, c = {}'.format(a, b, c), '\n')

a = b = c = d = 'Snow'
print('a = {}, b = {}, c = {}'.format(a, b, c), '\n')

# Комбинированное присваивание

a = 10
a = a + 30
print('a = {}'.format(a), '\n')

a = 10
a += 30
print('a = {}'.format(a), '\n')

a = 3
b = 5
a = a & b
print('a = {}, b = {}'.format(bin(a), bin(b),), '\n')

a = 3
b = 5
a &= b
print('a = {}, b = {}'.format(bin(a), bin(b),), '\n')

