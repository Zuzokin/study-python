import time


# Task 1
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Выполнение функции {func.__name__} заняло {end_time - start_time} секунд')
        return result

    return wrapper


@timer
def cool_func(number):
    k = 0
    for i in range(number):
        for j in range(number):
            if (i * j) % 17 == 0:
                k += 1
    return k


print(cool_func(1000))


# Task 2
def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]

    return wrapper


# Task 3
def logging(func):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            print(f'{func.__name__} {args} {kwargs}', file=log_file)
        return func(*args, **kwargs)

    return wrapper


@logging
@cache
def fibo(x):
    if x == 0 or x == 1:
        return 1
    return fibo(x - 1) + fibo(x - 2)


for n in range(50):
    print(n, fibo(n))


# Task 4
def retry(max_attempts, delay):
    def inside_func(func):
        def wrapper(*args, **kwargs):
            attempts_left = max_attempts
            while attempts_left > 0:
                result = func(*args, **kwargs)
                if result is not None:
                    return result
                attempts_left -= 1
                time.sleep(delay)

        return wrapper

    return inside_func


@retry(3, 1)
def say_hi():
    print('Hi!')


say_hi()
