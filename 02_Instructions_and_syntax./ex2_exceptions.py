# -*- coding: utf-8 -*-

# ///п///////////////////////////////////////////////////////
# //
# //               Исключеня - Exceptions
# //

# http://www.ilnurgi1.ru/docs/python/base/errors.html

# https://docs.python.org/3/library/exceptions.html

HEADLINE: str = ' ИСКЛЮЧЕНИЯ '

print('\n')
print(HEADLINE.center(40, '*'), '\n')

try:
    number = int(input("Введите целое число: "))
    print('Введено число      :', number)
    lst = ['A', 'B', 'C', 'D', 'F', 'G', 'H']
    print('Элемент {} равен {}'.format(number, lst[number]))
except ValueError:
    # выполнится при возникновении ошибки ValueError
    print('Ошибка! Вы ввели не число!')
except IndexError:
    # выполнится при возникновении ошибки IndexError
    print('Ошибка! Индекс не может быть больше шести!')
else:
    # выполнится если ошибок не прозошло
    print('Отлично! Ошибок не возникло!')
finally:
    # выполнится в любом случае
    print('Конец!')


