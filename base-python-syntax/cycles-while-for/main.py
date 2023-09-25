# Задача 1

def very_cool_method():
    x = int(input())
    while (x % 2) != 0 and (x % 10) != 5:
        x = int(input())


# Задача 2
def definitely_my_programm():
    for i in range(0, 10):
        print(i)


# Задача 3
def sum_of_odd_numbers_between_k_and_n():
    k = int(input())
    n = int(input())
    while k <= 0 or n <= 0:
        print('не будь капибарой, напиши положительные числа')
        k = int(input())
        n = int(input())
    s = 0
    for x in range(k, n + 1):
        if x % 2 == 1:
            s += x
    print(s)


# sum_of_odd_numbers_between_k_and_n() # ans => 768182441


# Задача 4
def factorial():
    n = int(input())
    while n < 0:
        print('не будь капибарой, напиши положительное число')
        n = int(input())
    fact = 1
    for x in range(1, n):
        fact *= x
    print(fact)


# factorial() # ans => 362880
