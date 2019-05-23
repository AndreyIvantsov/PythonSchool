# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //   Чтение файлов с использоанием циклов for и while
# //

HEADLINE: str = ' Чтение файлов с использоанием циклов for и while '

print('\n')
print(HEADLINE.center(80, '*'), '\n')

# Чтение файла

file = open('dat.txt', 'r')
print(file.read())
