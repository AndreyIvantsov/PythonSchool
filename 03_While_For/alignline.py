# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //               Align lines to file width
# //

from argparse import ArgumentParser
from os import system

SPACE_IN_TAB = 4
SPACE = '*'


def add_space_to_word(word: str, count_of_spaces=1):
    return str(list(word).extend(SPACE * count_of_spaces))


def align_line(line: tuple, width: int):

    if len(line) < 2:
        return str(line)

    count_of_spaces: int = len(line) - 1

    count_of_chars: int = 0

    for word in line:
        count_of_chars += len(word)

    full: int = (width - count_of_chars) // count_of_spaces

    part: int = (width - count_of_chars) % count_of_spaces

    if full > 0:
        str_line: str = (SPACE.join(line)).replace(SPACE, SPACE * full)
    else:
        str_line: str = (SPACE.join(line))

    lst_line = list(str_line)
    start = 0
    stop = len(lst_line)
    while part > 0:
        index = lst_line.index(SPACE, start, stop)
        lst_line.insert(index, SPACE)
        start = index + 2
        part -= 1

    return ''.join(lst_line)


def align_paragraph(paragraph: tuple, width: int):

    lines = []
    line = []
    total_len = 0

    for word in paragraph:

        line.append(word)
        total_len += len(word) + 1

        if total_len >= width:

            if len(line) > 1:
                last_word = line.pop(-1)

                # Отладка
                line.append('{}|'.format(line.pop(-1)))

                lines.append(align_line(tuple(line), width))
                # lines.append(SPACE.join(line))

                line.clear()
                line.append(last_word)
                total_len = len(last_word)

    lines.append(SPACE.join(line))

    return '\n'.join(lines)

    # print('\n'.join(lines))
    # print('------------------')
    # for s in lines:
    #     print(s)


def align_text_to_file(file_source, file_dest, line_width: int):

    fs = open(file_source, 'r')
    fd = open(file_dest, 'w')

    prev_line = fs.readline()
    prev_line.replace('\t', SPACE * SPACE_IN_TAB)
    paragraph: list = []

    for this_line in fs:

        paragraph.extend(prev_line.split())

        this_line.replace('\t', SPACE * SPACE_IN_TAB)

        if (prev_line[-1] == '\n' and this_line[0] == '\n') or \
                (prev_line[-1] == '\n' and this_line[0] == SPACE):
            if len(paragraph) > 0:
                s = align_paragraph(tuple(paragraph), line_width)
                # print(s, '\n')
                fd.writelines([s, '\n', '\n'])
                paragraph.clear()

        prev_line = this_line

    fs.close()
    fd.close()


def test():
    print('Test Ok!')


def main():
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('source_file', type=str, help='source file')
    parser.add_argument('dest_file', type=str, help='destination file')
    parser.add_argument('width', type=int, default=60, help='line width')
    parser.add_argument('-s', '--silent', dest='silent', action='store_true',
                        default=False, help='turn on silent mode')
    parser.add_argument('-t', '--test', dest='test', action='store_true',
                        default=False, help='turn on test mode')

    args = parser.parse_args()

    if args.test:
        test()
        return

    if not args.silent:
        print('Source file     : {}'.format(args.source_file))
        print('Destination file: {}'.format(args.dest_file))
        print('Line width      : {}'.format(args.width))

    print('1........10........20........30........40........50........60........70........80........90........100.......110.......120')
    print('|        |         |         |         |         |         |         |         |         |         |         |         |')

    align_text_to_file(args.source_file, args.dest_file, args.width)

    system('cat {}'.format(args.dest_file))


if __name__ == '__main__':
    main()
