# викторина
# Задаем участников

import random

famous_people_data = {
    'Vladimir Putin': '23.02.1945',
    'Sergey Shoigu': '09.05.1945',
    'Sergey Lavrov': '01.01.2000',
    'Dmitry Medvedev': '12.06.1980',
    'Vladimir Volodin': '08.03.1977',
    'Djoh Baiden': '04.07.1911',
    'Barak Abama': '15.08.1973',
    'Donald Tramp': '31.12.2000',
    'Bitcoin Uesdosovich': '12.11.2009',
    'Efirium Psaky': '22.04.1950',
}
# объявляем имена месяцам

month_name = [
    '',
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря',
]

# объявляем дни

day_names = [
    '',
    'первого',
    'второго',
    'третьего',
    'четвертого',
    'пятого',
    'шестого',
    'седьмого',
    'восьмого',
    'девятого',
    'десятого',
    'одиннадцатого',
    'двенадцатого',
    'тринадцатого',
    'четырнадцатого',
    'пятнадцатого',
    'шестнадцатого',
    'семнадцатого',
    'восемнадцатого',
    'девятнадцатого',
    'двадцатого',
    'двадцать первого',
    'двадцать второго',
    'двадцать третьего',
    'двадцать четвертого',
    'двадцать пятого',
    'двадцать шестого',
    'двадцать седьмого',
    'двадцать восьмого',
    'двадцать деватого',
    'тридцатого',
    'тридцать первого',
]

# Задаем условие для викторины

next_round = 'y'

while next_round == 'y':

    hit = 0
    lose = 0

    random_five_famous_names = random.sample(famous_people_data.keys(), 5)

    print(random_five_famous_names)

    for name in random_five_famous_names:

        correct_input = False

        while not correct_input:
            answer = input(f'Введите дату рождения для {name} в формате  dd.mm.yyyy: ')

            if len(answer) == 10:
                if '.' in answer:
                    if answer.count('.') == 2:
                        datas = answer.split('.')
                        if len(datas[0]) == len(datas[1]) == 2 and len(datas[2]) == 4:
                            if datas[0].isdigit() and datas[1].isdigit() and datas[2].isdigit():
                                correct_input = True
                            else:
                                print('Введены не числа')
                        else:
                            print(f'Неверная длина чисел др!')
                    else:
                        print(f'Ставьте ДВЕ точки!!!')
                else:
                    print(f'Дату ЧЕРЕЗ две точки!!!')
            else:
                print(f'Неверный формат даты рождения! {name} огорчен')

        if answer == famous_people_data[name]:
            hit += 1
            print('ВЕРНО!)')
        else:
            lose += 1
            true_datas = famous_people_data[name].split('.')
            print(
                f'НЕ ВЕРНО... {name} родился {day_names[int(true_data[0])]} {month_name[int(true_datas[1])]} {int(true_datas[2])} года')

    hit_percent = (100 * hit // (hit + lose))
    lose_percent = (100 * lose // (hit + lose))
    print(f'Верно: {hit} ({hit_percent}%), ошибок: {lose} ({lose_percent}%)!\n')

    if hit_percent == 100:
        print('100% Верных ответов! Вы знаток!!!')
        next_round = 'n'
    else:
        next_round = input('Хотите повторить? [y/n]: ')
        print()

