from functools import reduce


# Задача 1
def programm1():
    d = {'Женя': 89, 'Вася': 100, 'Марк': 71, 'Мария': 79}
    f = list(filter(lambda x: d[x] > 80, d))
    print(f)


# Задача 2
def list_to_cubed(list_of_nums):
    return list(map(lambda num: num ** 3, list_of_nums))


nums = [2, 4, 6, 8, 10]
print(list_to_cubed(nums))


# Задача 3
def find_numbers_less_when_zero(list_of_nums):
    return list(filter(lambda num: num < 0, list_of_nums))


nums = [-1, 4, -7, -8, -10, 1, 0]
print(find_numbers_less_when_zero(nums))


# Задача 4
def get_fact(number):
    if number < 0:
        print("введите положительно число")
    elif number == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, [i for i in range(number, 0, -1)])


print(get_fact(8))

nums = [2, 4, 6, 8, 0, 3, 4, 2, 3, 5, 1, 2]


# Задача 5
def find_max_elem_multiple_of_9(numbers):
    return reduce(lambda x, y: x if x > y else y, filter(lambda num: num ** 2 % 9 == 0, numbers))


print(find_max_elem_multiple_of_9(nums))
