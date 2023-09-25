# Задача 1
def better_programm_in_one_line():
    print(sum(number ** 2 for number in range(1, 101)))


# better_programm_in_one_line()

# Задача 2
def my_password():
    a = [i for i in range(0, 20, 2)]
    b = [x * 2 for x in a]
    c = b[::2]
    print(c)


# my_password()

# Задача 3
def find_quantity_of_even_numbers():
    gen_exp = (number for number in range(1, 21) if number % 2 == 0)
    print(len(list(gen_exp)))


# find_quantity_of_even_numbers()

# Задача 4
def another_quantity_of_even_numbers():
    numbers = [64, 8, 72, 1, 56, 78, 7, 59, 9, 80]
    gen_exp = (number for number in numbers[::2] if number % 2 == 0)
    print(len(list(gen_exp)))


# another_quantity_of_even_numbers()

# Задача 5
def div_for_7_and_11_without_rem():
    gen_exp = (number for number in range(1, 1001) if number % 7 == 0 or number % 11 == 0)
    result_list = list(gen_exp)
    print(result_list)
    print("количество таких чисел:", end=" ")
    print((len(result_list)))

# div_for_7_and_11_without_rem()
