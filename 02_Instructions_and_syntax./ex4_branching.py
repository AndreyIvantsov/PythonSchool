# -*- coding: utf-8 -*-

# //////////////////////////////////////////////////////////
# //
# //                Ветвление - branching
# //
# //          инструкции if-else-elif, логические
# //                операторы и выражения
# //

# if <условие>:
#   <болок 1>
# elif <условие>:
#   <блок 3>
# ...
# elif <условие>:
#   <блок N>
# else:
#   <блок N+1>

colors_dic = {
    'красный': 'red',
    'оранжевый': 'orange',
    'желтый': 'yellow',
    'зеленый': 'green',
    'голубой': 'blue',
    'синий': 'navy',
    'фиолетоый': 'violet'
}

en_color = ''

err_msg = ''

ru_color = input('Введите один из цветов радуги: ').lower()

if ru_color == 'красный':
    en_color = colors_dic['красный']
elif ru_color == 'оранжевый':
    en_color = colors_dic['оранжевый']
elif ru_color == 'желтый':
    en_color = colors_dic['желтый']
elif ru_color == 'зеленый':
    en_color = colors_dic['зеленый']
elif ru_color == 'голубой':
    en_color = colors_dic['голубой']
elif ru_color == 'синий':
    en_color = colors_dic['синий']
elif ru_color == 'фиолетоый':
    en_color = colors_dic['фиолетоый']
else:
    err_msg = 'Ошибка! Не правильно указан цвет!'

if en_color != '':
    print('рус: {} -> en: {}'.format(ru_color, en_color))

if err_msg != '':
    print(err_msg)

# следующий урок 5
