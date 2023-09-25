import copy
import sys


# Задача 1
def what_is_output():
    R = [45, 84, 10, 58]
    A = R
    R[0] = 54
    print(A[0] + R[0])  # ans => 108


what_is_output()  # ans => 108


# Задача 2
def copy_of_array():
    print('Введите 5 значений')
    lst = [int(input()) for num in range(5)]
    lst_slice = lst[:]
    lst_copy = lst.copy()
    lst_copy_copy = copy.copy(lst)
    lst_deepcopy = copy.deepcopy(lst)
    lst_cast = list(lst)
    #print(f"ans: number of array copies: 5, sum of numbers: {sum(lst)} (should be 35)")
    print(f"5 {sum(lst)}")

copy_of_array() # => 5 35


# Задача 3
def what_is_result():
    AR = [[90, 99, 109, 119]] * 4
    AR[0][0], AR[3][3] = 890, 76
    print(AR[1][0] + AR[2][3])


what_is_result()  # ans => 966

# Задача 4
animals = ["cat", "cat", "dog", "dog", "bird", "capybara", "capybara", "capybara"]


def count_animal_and_make_dict(animals_lst):
    animals_dict = dict()
    for animal in animals_lst:
        if animal not in animals_dict:
            animals_dict[animal] = 1
        else:
            animals_dict[animal] += 1
    for animal in animals_dict:
        print((f'Количество ссылок для {animal}: {sys.getrefcount(animal)}'))
    for value in animals_dict.values():
        print((f'Количество ссылок для {value}: {sys.getrefcount(value)}'))


count_animal_and_make_dict(animals)

# Задача 5
backpack = ["capybara", "capyraba", "capyba", "capyba", "capybara",
            2999, 2999, "capybara", [7, 7, 7], [7, 7, 7], [7, 7, 7],
            [7, 7, 7]] + [[8, 8]] * 5


def count_same_and_equal_elements(lst):
    same_counter = 0
    equal_counter = 0
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if i < j:
                if lst[i] == lst[j]:
                    equal_counter += 1
                if lst[i] is lst[j]:
                    same_counter += 1
    print(same_counter, equal_counter)


count_same_and_equal_elements(backpack)


# Задача 6
def make_rec_caesar():
    rec_caesar = []
    ingredients_list = ['lettuce', 'chicken', 'cheese', 'sauce', 'tomatoes', 'croutons']
    rec_caesar = [ingredient for ingredient in ingredients_list]
    rec_caesar.append(rec_caesar)
    update_rec_caesar = rec_caesar.copy()
    rec_caesar.append('salt')
    rec_caesar.append('pepper')
    # представим, что в первом случае 127 обращений :)
    print(update_rec_caesar[6][6][6][6][6][6][6][6][6][6][6][6][6][6][6][4], update_rec_caesar[6][-1])

make_rec_caesar() # ans = tomatoes pepper
