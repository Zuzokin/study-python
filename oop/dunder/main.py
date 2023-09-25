import enum
import math
import random


# Task 1
def infiltrate():
    pass


SIGNATURE = "-~=$([{PETR}])$=~-"


class SignedMessage:

    def __new__(cls, *args, **kwargs):
        infiltrate()
        return object.__new__(cls)

    def __init__(self, message, signature=SIGNATURE):
        self.signature = signature
        self.message = message

    def __str__(self):
        return f"{self.message} {self.signature}"

    def __add__(self, obj):
        # return f"{self.message}{other}"
        return SignedMessage(self.message + obj.message, self.signature)


# # выводится "Hello -~=$([{PETR}])$=~-"
# print(SignedMessage("Hello ", SIGNATURE))
#
# # выводится "world! -~=$([{PETR}])$=~-"
# print(SignedMessage("world!", SIGNATURE))
#
# # выводится "Hello world! -~=$([{PETR}])$=~-"
# print(SignedMessage("Hello ", SIGNATURE) + SignedMessage("world!", SIGNATURE))


# Task 2
class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other_vector):
        return Vector2(self.x + other_vector.x, self.y + other_vector.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __sub__(self, other_vector):
        return Vector2(self.x - other_vector.x, self.y - other_vector.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"{{{self.x}, {self.y}}}"

    def __eq__(self, other_vector):
        return self.x == other_vector.x and self.y == other_vector.y

    def __ne__(self, other_vector):
        #       return not (self.x == other_vector.x and self.y == other_vector.y)
        return not (self == other_vector)

    def __mul__(self, other_vector):
        return self.x * other_vector.x + self.y * other_vector.y


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other_vector):
        return Vector3(self.x + other_vector.x, self.y + other_vector.y, self.z + other_vector.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __sub__(self, other_vector):
        return Vector3(self.x - other_vector.x, self.y - other_vector.y, self.z - other_vector.z)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __str__(self):
        return f"{{{self.x}, {self.y}, {self.z}}}"

    def __eq__(self, other_vector):
        return self.x == other_vector.x and self.y == other_vector.y and self.z == other_vector.z

    def __ne__(self, other_vector):
        return not (self == other_vector)

    def __mul__(self, other_vector):
        return self.x * other_vector.x + self.y * other_vector.y + self.z * other_vector.z


# Проверка реализации класса Vector 3
# print(Vector3(1, 2, 3) + Vector3(3, 4, 5) == Vector3(4, 6, 8))
# print(-Vector3(1, 0, -1) == Vector3(-1, 0, 1))
# print(Vector3(7, 7, 7) - Vector3(3, 2, 1) == Vector3(4, 5, 6))
# print(abs(Vector3(3, 4, 0)) == 5)
# print(str(Vector3(0, 5, 2)) == "{0, 5, 2}")
# print(Vector3(1, 1) != Vector3(2, 2))


# Task 3
class Rarity(enum.IntEnum):
    common = 0
    rare = 1
    epic = 2
    legendary = 3


class Item:
    def __init__(self, ID, price, rarity, color):
        try:
            if ID < 0:
                raise ValueError
            if price < 0:
                raise ValueError
        except ValueError:
            # не лучшая обработка исключения, но так программа не сломается
            print("Введен отрицательный параметр")
            ID = abs(ID)
            price = abs(price)

        self.ID = ID
        self.price = price
        self.rarity = rarity
        self.color = color

    # Сравнение по ID, цене, редкости и цвету
    # в решении это реализовано элегантнее
    def __lt__(self, other):
        if self.ID < other.ID:
            return True
        elif self.ID == other.ID:
            if self.price < other.price:
                return True
            elif self.price == other.price:
                if self.rarity < other.rarity:
                    return True
                elif self.rarity == other.rarity:
                    if self.color < other.color:
                        return True
        return False

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not (self == other)

    def __eq__(self, other):
        return (
                self.ID == other.ID
                and self.price == other.price
                and self.rarity == self.rarity
                and self.color == other.color
        )

    @staticmethod
    def generate_random_item():
        return Item(
            random.randint(0, 128),
            random.randint(0, 100),
            random.choice(list(Rarity)),
            ("%06x" % random.randint(0, 0xFFFFFF)).upper()
        )

    @staticmethod
    def generate_items(number):
        return [Item.generate_random_item() for _ in range(number)]


# создаю 2 предмета и проверяю операторы сравнения
new_item = Item(-1, 1000, Rarity.common, "FFFFFF")
undefined_item = Item(128, 1000, Rarity.legendary, "FFF1FF")
print(new_item == undefined_item)
print(new_item != undefined_item)
print(new_item >= undefined_item)
print(new_item <= undefined_item)
print(new_item > undefined_item)
print(new_item < undefined_item)

# проверяю метод generate_random_item
item1 = Item.generate_random_item()
print(print(item1.ID, item1.price, item1.rarity, item1.color))
# проверяю метод generate_random_items и sort
items = Item.generate_items(229)
items.sort()
list(print(item.ID, item.price, item.rarity, item.color) for item in items)
