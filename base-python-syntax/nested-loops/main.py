# задача 1
def print_multiplication_table():
    for i in range(1, 11):
        print()
        for j in range(1, 11):
            print(f'{i} * {j} = {i * j}', end='   ')


# print_multiplication_table() # почти ровно :)

# Задача 2 не получилось сделать так, чтобы совпало с ответом, получается 19 вместо 26
# PS после жесткого дебагинга понял, что проблема в переборе значений, как исправить хз
# todo: исправить перебор (line 24 x < y)
# PSS прикольная подсветка todo
def find_pyth_triples_in_range():
    print('Напишите левую границу')
    left = int(input())
    print('Напишите правую границу')
    right = int(input())
    counter = 0
    for x in range(left, right + 1):
        for y in range(left, right + 1):
            k = (x ** 2 + y ** 2) ** 0.5
            if k == int(k) and x < y:
                # print(f'{x}^2 + {y}^2 = {int(k)}^2')
                counter += 1
    print(f'Всего троек: {counter}')


# Другое решение задачи 2
def find_pyth_triples_in_range_another():
    print('Напишите левую границу')
    left = int(input())
    print('Напишите правую границу')
    right = int(input())
    counter = 0
    for x in range(left, right + 1):
        for y in range(left, right + 1):
            for k in range(left, right + 1):
                if x ** 2 + y ** 2 == k ** 2:
                    counter += 1
    print(counter)


# find_pyth_triples_in_range() # ans => 19
# find_pyth_triples_in_range_another() # ans => 26

# жесткий дебагинг
# def compare_two_method():
#     left = 10
#     right = 50
#     first_counter = 0
#     second_counter = 0
#     first_method_triples = []
#     for x in range(left, right + 1):
#         for y in range(left, right + 1):
#             k = (x ** 2 + y ** 2) ** 0.5
#             if k == int(k) and x < y:
#                 # print(f'{x}^2 + {y}^2 = {int(k)}^2')
#                 first_method_triples.append([x, y, int(k)])
#                 first_counter += 1
#
#     second_method_triples = []
#     for x in range(left, right + 1):
#         for y in range(left, right + 1):
#             for k in range(left, right + 1):
#                 if x ** 2 + y ** 2 == k ** 2:
#                     second_counter += 1
#                     second_method_triples.append([x, y, k])

#     print(first_counter)
#     print(second_counter)
#     first_method_triples.sort()
#     second_method_triples.sort()
#     print(first_method_triples)
#     print(second_method_triples)

# compare_two_method()


# Задача 3
def find_friendly_numbers():
    n = int(input())
    dictionaty = dict()
    # заполняю словарь суммами делителей
    for number in range(n):
        dictionaty[number] = sum(divider for divider in range(1, round(number / 2) + 1) if number % divider == 0)
    # прохожусь по всем keys и проверяю если key совпадает с значением ключа value, то пара найдена
    for key in dictionaty:
        value = dictionaty[key]
        if dictionaty.get(value) == key and value != key:
            print(key, dictionaty[key])
            dictionaty[key] = "А всё"  # костыль, но теперь выводит 1 пару :)


# find_friendly_numbers()


# Задача 4
def quantity_of_armstrong_numbers():
    n = 4  # в тз не сказано, как вводится число :)
    if n == 1:
        print(list(num for num in range(1, 10)))
    else:
        for number in range(10 ** (n - 1), 10 ** n):
            temp_summa = 0
            for sign in str(number):
                temp_summa += int(sign) ** n
            if temp_summa == number:
                print(number, end=' ')

# quantity_of_armstrong_numbers()
