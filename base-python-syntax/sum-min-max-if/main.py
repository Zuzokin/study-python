# Задача 1
def first_problem():
    n = int(input())
    for i in range(n + 1):
        if i % 3 == 0 and i % 6 != 0:
            print(i)


# first_problem()

# Задача 2

def second_problem():
    n = int(input())
    for i in range(10, n + 1):
        if i % 2 == 0:
            print(i)


# second_problem()

# Задача 3
def third_problem():
    n = int(input())
    if n % 2 == 0:
        counter = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                counter = counter + 1
        print(counter)
    else:
        summa = 0
        for i in range(1, n + 1):
            if i % 2 == 1:
                summa = summa + i
        print(summa)


# third_problem()

# Задача 4
def fourth_problem():
    n = int(input())
    if n % 3 == 0:
        print("еще одно число")
        m = int(input())
        counter = 0
        for i in range(1, n + 1):
            if i % m == 0:
                counter = counter + 1
        print(counter)
    else:
        for i in range(1, n + 1):
            print(n ** i, end=" ")


# fourth_problem()

# Задача 5
def fifth_problem():
    a = int(input())
    b = int(input())
    n = int(input())
    numbers_list = []
    counter = 0
    for i in range(n):
        numbers_list = numbers_list + [int(input())]
    for hypotenuse in numbers_list:
        if hypotenuse > 10 and (hypotenuse % 3 == 0 or hypotenuse % 4 == 0):
            if hypotenuse ** 2 == a ** 2 + b ** 2:
                counter = counter + 1
    print(counter)


# fifth_problem()
