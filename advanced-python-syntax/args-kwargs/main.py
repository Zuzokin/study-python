# Задача 1
def sum_numbers(*numbers):
    return sum(numbers)


print(sum_numbers(1, 2, 3, 4, 5))


# Задача 2
def print_kwargs(**kwargs):
    for i, j in kwargs.items():
        print(f'{i}: {j}')


print_kwargs(name='Alice', age=25, country='USA')


# Задача 3
def filter_by_length(min_length, *strs):
    result = []
    for string in strs:
        if len(string) >= min_length:
            result.append(string)
    return result


strings = ["hello", "world", "how", "are", "you"]
print(filter_by_length(4, *strings))


# Задача 4
def calculate_total_price(price, **discounts):
    return price - sum(discounts.values()) * price * 0.01


print(calculate_total_price(100, student=10, coupon=20))
print(calculate_total_price(200, holiday=25))
print(calculate_total_price(500))


# Задача 5
def custom_print(*args, sep=' ', end='\n', **kwargs):
    result = ''
    sep = str(sep)
    end = str(end)
    for arg in args:
        result += str(arg) + sep
    for key, value in kwargs.items():
        result += f'{key}={value}{sep}'
    return result[:-len(sep)] + end


print(custom_print(1, 2, 3, a=4, b=5, sep='-', end='!'))
print(custom_print('Hello', 'World', sep=' '))
print(custom_print('apple', 'banana', 'cherry', sep=', '))
print(custom_print(a=1, b=2, end='...'))
