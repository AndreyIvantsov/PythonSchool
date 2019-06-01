# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //      Чтение файлов с использоанием for и итератора
# //

HEADLINE: str = ' Чтение файлов с использоанием for и итератора  '

print('\n')
print(HEADLINE.center(80, '*'), '\n')

# Чтение с использованием for
file = open('dest.txt', 'r')
for line in file.readlines():
    print(line, end='')
file.close()

# Чтение с использованием итератора самый быстрый способ
print('\n')
print('+' * 60)
file = open('dest.txt', 'r')
for line in file:
    print(line, end='')
file.close()

