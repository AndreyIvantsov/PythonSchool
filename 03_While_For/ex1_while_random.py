# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //                      Цикл while
# //

# Игра угадай число

from random import randint

START = 1
END = 15
count = 1
game_over: bool = False

rnd_number = randint(START, END)

print("""
*********************************
*       Игра угадай число       *
*         от {:0>3} до {:0>3}         *
*********************************
""".format(START, END))

while not game_over:
    try:
        input_number = int(input('Попытка № {:0>3}. Введите число: '.format(count)))
    except ValueError:
        print('Ошибка! Введено не целое число!')
        continue
    if rnd_number == input_number:
        print('Вы угадали! число {}. Попыток {}'.format(rnd_number, count))
        game_over = True
    else:
        if rnd_number > input_number:
            print('Загаданное число больше...')
        elif rnd_number < input_number:
            print('Загаданное число меньше...')
        count += 1
