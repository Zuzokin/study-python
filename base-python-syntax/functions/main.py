# Задача 1
def sum_list(lst):
    return sum(lst)


ary = [1, 7, 42, 12, 10, 1, 4, 0]
print(sum_list(ary))  # ans => 77


# Задача 2
def is_number_in_range(number: int, left: int, rigth: int):
    return left <= number <= rigth


print(is_number_in_range(7, 1, 9))  # ans => True


# Задача 3
def is_number_perfect(number: int):
    digits_sum = sum([digits for digits in range(1, round(number / 2 + 1)) if number % int(digits) == 0])
    return digits_sum == number


print(is_number_perfect(8128))  # ans => True


# Задача 4
def is_number_polindrome(number):
    number_str = str(number)
    if len(number_str) == 0 or len(number_str) == 1:
        return True
    if number_str[0] == number_str[-1]:
        number_str = number_str[1:-1]
        return is_number_polindrome(number_str)
    else:
        return False


print(is_number_polindrome(1234567899876554321))  # ans => False


# Задача 5
def is_prime_number(number: int):
    if number == 1:
        return True
    for divider in range(2, round(number / 2 + 1)):
        if number % divider == 0:
            return False
    return True


print(is_prime_number(123321))  # ans => False


# Задача 6
def fibo(num: int):
    if num == 0:
        return 0
    if num == 1 or num == 2 or num == 3:
        return 1
    return fibo(num - 1) + fibo(num - 2)


print(fibo(10))
