# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //          Выравнивание строк файла по ширине
# //


def line_align(line: str):
    if len(line) >= WIDTH:
        return line
    else:
        count_space = 1
        pos = 0
        words = line.expandtabs().split()
        print(words)
        width = 0
        for word in words:
            width += len(word)
        print(width)
        print(len(words))

        # while len(line) < WIDTH:
        #     sub = ' ' * count_space
        #     pos = line.index(sub, pos)
        # new_line = '{} {}'.format()


HEADLINE: str = ' Выравнивание строк файла по ширине '

print('\n')
print(HEADLINE.center(80, '*'), '\n')

FILE_SOURCE = 'dat.txt'
FILE_DEST = 'dat_res.txt'
WIDTH = 100

file_source = open(FILE_SOURCE, 'r')

for line in file_source:
    print(line, end='')
    line_align(line)
    break






