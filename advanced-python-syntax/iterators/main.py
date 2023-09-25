# Задача 1
a = [2, 4, 6, 8]
b = {1, 3, 5, 7}
a_itera = iter(a)
b_iterb = iter(b)
next(iter(a_itera))
print(next(a_itera), next(b_iterb))
next(b_iterb)
print(next(b_iterb), next(iter(iter(iter(a_itera)))))
# ans => 4 1
#        5 6

# Задача 2
line = 'ППШ'
iterator = iter(line)
for x in iterator:
    print(x)
# ans => П
#        П
#        Ш

# Задача 3
d = {1: 'bee', 2: 'raccoon', 3: 'snake'}
iterator = iter(d)
print(d[next(iterator)])
# ans => bee

# Задача 4
a = [int(s) for s in range(1, 20)]
iterator = iter(a)
print(9 in iterator)
print(9 in iterator)
# ans => True False

# Задача 5
a = (i ** 2 for i in range(10) if i % 3 != 0)
print(next(a))
print(next(a))
print(next(a))


# ans => 1 4 16

# Задача 6
def squared_numbers():
    gen_exp = (i ** 2 for i in range(1, 6))
    iterator1 = iter(gen_exp)
    print(next(iterator1))
    next(iterator1)
    print(next(iterator1))
    next(iterator1)
    print(next(iterator1))


squared_numbers()


# ans => 1 9 25


# Задача 7
def deck_of_cards():
    values = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    cards_iterator = (str(value) + " " + suit for value in values for suit in suits)
    # for card in cards_iterator:
    #     print(card)
    counter = 0
    while counter < 36:
        # input()
        counter += 1
        print(next(cards_iterator))
    print("Stop iteration")


deck_of_cards()
