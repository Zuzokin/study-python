# region Task 3
import sys

sys.setrecursionlimit(1200)


def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n - 1, sum + n)


print(recursive_function(1000, 0))
# endregion

# region Task 4
import re


def find_digits_in_string(_text):
    return re.findall(r'\d+', text)


text = 'ул. Кутузовская, дом № 13, корпус 3, квартира 98'

print(find_digits_in_string(text))

# endregion

# region Task 5

from random import randint as rnd, choice as chc

array = []
for _ in range(10):
    array.append(rnd(1, 100))
print(array, chc(array), sep='\n')
# endregion

# region Task 6
import math

a = 1
b = 4
c = -5


def find_quadratic_equation_roots(a, b, c):
    D = b * b - 4 * a * c
    try:
        if D < 0:
            return None
        if D == 0:
            return -b / (2 * a)

        sqrtD = math.sqrt(D)
        x1 = (-b + sqrtD) / (2 * a)
        x2 = (-b - sqrtD) / (2 * a)
        return x1, x2
    except ZeroDivisionError:
        print("коэффициент a равен 0")


print(find_quadratic_equation_roots(a, b, c))
# endregion

# region Task 7
from datetime import datetime

print(datetime.now().time())

# endregion

# region Task 8
from datetime import date, timedelta

d1 = date.fromisoformat('2023-06-09')
d2 = date(2023, 5, 31)
if d1 > d2:
    delta = d1 - d2
    print(delta.days)
    delta2 = timedelta(days=30)
    print((d1 + delta2).weekday() + 1)
# endregion

# region Task 9
import py_version

py_version.py_version()
# endregion

# region Task 10
import calculator as calc


def calculator():
    print("Калькулятор может +, -, *, /"
          "\nВведите выражение с 2мя операндами через пробел"
          "\nНапример: 7 * 5"
          "\nДля выхода введите 'exit'"
          )
    while True:
        expression = input('Введите выражение')
        match expression.split():
            case [num1, '+', num2]:
                print(calc.add(float(num1), float(num2)))
            case [num1, '-', num2]:
                print(calc.sub(float(num1), float(num2)))
            case [num1, '*', num2]:
                print(calc.mul(float(num1), float(num2)))
            case [num1, '/', num2]:
                print(calc.div(float(num1), float(num2)))
            case ['exit']:
                print('Выход из калькулятора')
                break
            case _:
                print('Неверная команда')


# calculator()

# endregion
# region Task 11
from imp_modules import imp_mods

moduleNames = ('random', 'math')
imp_mods(moduleNames, globals())

print(math.factorial(random.randint(1, 10)))

# endregion
# region Task 12
from geometry import *

print(triangle(3, 2, 4))
print(square(12))
print(circle())

# endregion
