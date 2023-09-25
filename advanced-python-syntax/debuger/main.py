# Задание 1
def f(a, b):
    return 18 * a * b


print(f(1, 13))
# Задание 2
summa = 0
for i in range(1, 11):
    summa += i
print("The sum is: ", summa)


# Задание 3
def is_even(n):
    if int(n) % 2 == 0:
        print(n, " is even")
    else:
        print(n, " is odd")


is_even('4')


# Задание 4
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))


# Задание 5
def is_palindrome(s):
    s = s.lower()
    for sign in range(len(s)):
        if s[sign] != s[len(s) - sign - 1]:
            return False
    return True


print(is_palindrome('Коссок'))


# Задание 6
def multiplylist(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
    for el in range(len(lst)):
        result = result * lst[el]
    return result


print(multiplylist([1, 2, 3, 4, 5, 100, 6]))
