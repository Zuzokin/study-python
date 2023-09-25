# Task 2
def summa(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + summa(numbers[1:])


def is_even(number):
    return number % 2 == 0


def get_even_numbers(numbers):
    f = is_even
    even_numbers = list(filter(f, numbers))
    return even_numbers


def sum_even_numbers_functional(numbers):
    return summa(get_even_numbers(numbers))


numbers = (14, 93, 19, 38, 18, 51, 77)
print(sum_even_numbers_functional(numbers))


# Task 3
def sum_even_numbers(numbers):
    result = 0
    for number in numbers:
        if number % 2 == 0:
            result += number
    return result


numbers = [60, 84, 9, 49, 7, 85, 38]
print(sum_even_numbers(numbers))
