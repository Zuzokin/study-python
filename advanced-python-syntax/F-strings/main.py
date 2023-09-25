import re


# Задача 1
def give_red_diploma():
    names = ['Александр', 'Алекс', 'Альберт']
    surnames = ['Вотяк', 'Вотяков', 'Вотякович']
    patronymic = 'Романович'
    for name in names:
        for surname in surnames:
            print(f"Диплом с отличием вручается {name}у {surname}у {patronymic}у.")


# give_red_diploma()


# Задача 2
def generate_car_id():
    flag = True
    letters = ''
    first_numbers = ''
    second_numbers = ''
    while flag:
        print('Введите 3 буквы')
        letters = input()
        if re.fullmatch(r'[A-Z]{3}', letters):
            flag = False
        else:
            print('некорреткно введены данные')
    flag = True
    while flag:
        print('Введите цифвы')
        first_numbers = input()
        if re.fullmatch(r'\d{1,4}', first_numbers):
            flag = False
        else:
            print('некорреткно введены данные')
    flag = True
    while flag:
        print('Введите следующие цифры')
        second_numbers = input()
        if re.search(r'\d{1,3}', second_numbers):
            flag = False
        else:
            print('некорреткно введены данные')
    return f'{letters}{first_numbers:>04}-{second_numbers:>03}'


# print(generate_car_id())


# Задача 3
def column_summation():
    print('Введите первое слогаемое')
    first_num = input()
    print('Введите второе слогаемое')
    second_num = input()
    if len(first_num) < len(second_num):
        first_num, second_num = second_num, first_num
    print(f'{first_num:>9}')
    print(f'{second_num:>9}')
    print(f'{(int(first_num) + int(second_num)):>9}')


# column_summation()


# Задача 4
def bank_deposit_calculator():
    print('Введите процент выплат каждый месяц')
    r = int(input())
    print('Введите количество месяцев')
    k = int(input())
    money = 100_000_000
    for i in range(k):
        money += money * r * 0.01
    print(f'{money:,.2f}')


# bank_deposit_calculator()
# Задача 5
def debug_mult_table():
    for a in range(1, 101):
        for b in range(1, 101):
            result = a * b
            if "0" in str(result):
                print(f"[DEBUG] {a=} {b=} {result=}")


# debug_mult_table()


# Задача 6
def gen_wrong_minecraft_ip():
    a, b, c, d = map(int, input().split())
    substitutions = ('{:08b}', '{:b}', '{:o}', '{}', '{:02X}')
    for i in substitutions:
        print((f'{i}.' * 4)[:-1].format(a, b, c, d))


gen_wrong_minecraft_ip()
