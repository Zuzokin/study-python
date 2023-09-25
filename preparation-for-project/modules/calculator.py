def add(a, b):
    return a + b


# Вычитание
def sub(a, b):
    return a - b


# Умножение
def mul(a, b):
    return a * b


# Деление
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Деление на 0!'
