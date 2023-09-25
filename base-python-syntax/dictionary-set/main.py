import re


# Задача 1
def get_dict_with_equal_value(lst):
    dictionary = dict()
    for obj in lst:
        dictionary[obj] = obj
    return dictionary


lst_for_1st_task = [1, 2, 3, 4, 5]
print(get_dict_with_equal_value(lst_for_1st_task))  # ans => {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


# Задача 2
def get_dict_with_square_value(number):
    dictionary = dict()
    for i in range(1, number + 1):
        dictionary[i] = i * i
    return dictionary


number_for_second_task = 5
print((get_dict_with_square_value(number_for_second_task)))


# Задача 3
def multiply_dict_values(dictionary: dict):
    product = 1
    for value in dictionary.values():
        product *= value
    return product


dictionary_for_third_task = {'data10': 375, 'data20': 567, 'data30': -37, 'data40': 21}
print(multiply_dict_values(dictionary_for_third_task))


# Задача 4

def get_quantity_of_punctuation_marks(line: str) -> dict:
    dictionary = dict.fromkeys([".", ":", ";", "!", "?", ","], 0)
    for sign in line:
        if sign in dictionary:
            dictionary[sign] += 1
    return sum(dictionary.values())


big_line = ("Летний день - это день, когда наступает летнее солнцестояние и длительность дня достигает своего "
            "максимума. В разных странах и регионах летние дни могут иметь разную продолжительность и "
            "характеризоваться разными погодными условиями. Вообще, летние дни обычно ассоциируются с теплой и ясной "
            "погодой, зелеными лугами, пляжами, купанием в море или озере, пикниками и барбекю. В летние дни люди "
            "часто отдыхают и проводят время на открытом воздухе, занимаются спортом, путешествуют и открывают новые "
            "места!")
print(get_quantity_of_punctuation_marks(big_line))  # ans => 12


# Задача 5
def get_unique_numbers(line: str):
    if not re.search(r'[^\W\d_]', line):  # куда я полез... думаю рановато для regex
        print('NO')
    very_cool_set = set(line)
    list_of_digits = [charcter for charcter in very_cool_set if charcter.isdigit()]
    list_of_digits.sort()
    for digits in list_of_digits:
        print(digits, end=' ')


get_unique_numbers("kn1mb9c7c5cv5cc9cvv7cx9sd8nm4cz2bm4k6hf9d")
