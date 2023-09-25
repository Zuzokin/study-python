# Задача 1
def sum_of_2_numbers():
    ary = []
    print('Напишите n')
    n = int(input())
    print('Напишите m')
    m = int(input())
    ary.append(n)
    ary.append(m)
    print(sum(ary))


# sum_of_2_numbers()

# Задача 2
def get_first_and_last_word():
    line = input()
    words_list = line.split()
    print(words_list[0], words_list[-1])


# get_first_and_last_word()


# Задача 3
def get_longest_word():
    line = input()
    words_list = line.split()
    longest_word = ""
    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)


# get_longest_word()

# Задача 4
def find_sum():
    n = int(input())
    numbers_list = []
    for number in range(1, n + 1):
        if number % 3 == 0 or number % 5 == 0:
            numbers_list.append(number)
    print(sum(numbers_list))


# find_sum()

# Задача 5 мне религия не позволяет писать здесь что-то сложнее O(n)
def find_most_frequently_word():
    line = input()
    words_list = line.split()
    dictionary = dict()

    for word in words_list:
        if word not in dictionary:
            dictionary[word] = 0
        else:
            dictionary[word] += 1
    # не до конца понимаю как именно работает key=dictionary.get, но оно работает
    print(max(dictionary, key=dictionary.get))


# find_most_frequently_word()
