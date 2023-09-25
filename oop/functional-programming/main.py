import functools


# Task 1
def factorial(n: int):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(6))


# Task 2
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def is_prime_ver2(n, i=2):
    if n < 2:
        return False
    elif i * i > n:
        return True
    elif n % i == 0:
        return False
    else:
        return is_prime_ver2(n, i + 1)


# Task 3
def filter_odd(numbers: tuple):
    odd_numbers = tuple(filter(lambda number: number % 2 == 1, numbers))
    return odd_numbers


print(filter_odd((1, 2, 3, 4, 5, 6, 7)))


# Task 4
def map_square(numbers: tuple):
    squared_numbers = tuple(map(lambda number: number ** 2, numbers))
    return squared_numbers


print(map_square((1, 2, 3, 4, 5, 6)))


# Task 5
def reduce_sum(numbers: tuple):
    summa = functools.reduce(lambda x, y: x + y, numbers)
    return summa


print(reduce_sum((1, 2, 3, 4, 5, 6, 7, 8)))


# Task 6
def partial_apply(func):
    def partial_func(x):
        def wrapper(y):
            return func(x, y)

        return wrapper

    return partial_func


# Task 7
def compose(f, g):
    def h(*args):
        return g(f(*args))

    return h


# Task 8
def create_function_with_arguments(func, *arguments):
    def new_func(func):
        return func(*arguments)

    return new_func


# Task 9
def compose_functions(functions: tuple):
    def composed_function(arg):
        get_compose_func = compose
        result_composed_func = functools.reduce(get_compose_func, functions)
        return result_composed_func(arg)

    return composed_function


def func_creator(number_to_sum):
    return lambda x: x + number_to_sum


# для проверки работоспособности compose_functions создаю кортеж функций и вызываю с аргументом 1
tuple_to_create_func = (1, 3, 6, 7, 123)
tuple_of_functions = tuple(map(func_creator, tuple_to_create_func))

f = compose_functions(tuple_of_functions)
print(f(1))
