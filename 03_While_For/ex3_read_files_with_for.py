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
file.close()

# Посимвольное чтение файла

file = open('dat.txt', 'r')
print('-' * 20)
while True:
    ch = file.read(1)
    if not ch:
        break
    print(ch, end='')
file.close()

print('\n\n', '*'* 20)
for ch in open('dat.txt', 'r'):
    print(ch, end='')


# Чтение строками

print('\n\n', '+' * 20)
file = open('dat.txt', 'r')
while True:
    lines = file.readline()
    if not lines:
        break
    print(lines, end='')
file.close()


# Чтение блоками по байтам

print('\n\n', '=' * 20)
file = open('dat.txt', 'r')
while True:
    byte = file.read(20)
    if not byte:
        break
    print(byte)
file.close()


