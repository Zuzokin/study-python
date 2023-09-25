import random


# Task 1
class CoffeMachine:
    def __init__(self, water_level, coffee_level, milk_level, sugar_level=0, cups=0):
        self.cups = cups
        self.sugar_level = sugar_level
        self.milk_level = milk_level
        self.coffee_level = coffee_level
        self.water_level = water_level

    def add_water(self, amount):
        self.water_level += amount

    def add_coffee(self, amount):
        self.coffee_level += amount

    def add_milk(self, amount):
        self.milk_level += amount

    def add_sugar(self, amount):
        self.sugar_level += amount

    def add_cups(self, number):
        self.cups += number

    def check_resources(self):
        if (
                self.water_level > 0
                and self.coffee_level > 0
                and self.milk_level > 0
                and self.sugar_level > 0
                and self.cups > 0
        ):
            return True
        else:
            return False

    def make_coffee(self):
        if self.check_resources():
            self.water_level -= 1
            self.coffee_level -= 1
            self.milk_level -= 1
            self.sugar_level -= 1
            self.cups -= 1
            print('Кофе готов!')
        else:
            print('Недостаточно ингредиентов!')


# Task 2
class PhotoCamera:
    def __init__(self, brand="", model="", resolution=(0, 0), memory_capacity=0, photos=[], is_on=False):
        self.photos = photos
        self.memory_capacity = memory_capacity
        self.is_on = is_on
        self.resolution = resolution
        self.model = model
        self.brand = brand

    def take_photo(self):
        print(f'Сделана фотография с разрешением {self.resolution[0]}x{self.resolution[1]}.')

    def get_camera_info(self):
        print(f'Марка:{self.brand}, Модель: {self.model}, Разрешение: {self.resolution[0]}x{self.resolution[1]}')

    def turn_on(self):
        self.is_on = True
        print('Фотокамера  включена')

    def turn_off(self):
        self.is_on = False
        print('Фотокамера  выключена')

    def is_camera_on(self):
        return self.is_on

    def store_photo(self, photo):
        if self.memory_capacity < len(self.photos):
            self.photos.append(photo)
            return True
        return False

    def view_photos(self):
        list(map(lambda photo: print(photo), self.photos))

    def clear_memory(self):
        self.photos = []


# Task 3
class Revolver:
    # количество слотов в барабане;
    def __init__(self, chambers=6):
        if chambers > 6:
            print('Барабан не может иметь больше 6 слотов, ставлю максимальное значение - 6')
            # Я бы тут поспорил, что максимум 6 слотов, но тз есть тз:)
            self.__chambers = 6
        else:
            self.__chambers = chambers
        # лист патронов в барабане;
        self.__bullets = [None] * chambers
        # указатель на текущий слот в барабане
        self.__chamber_pointer = 0

    def add_bullet(self, bullet):
        if self.__bullets[self.__chamber_pointer] is None:
            self.__bullets[self.__chamber_pointer] = bullet
            self.__chamber_pointer = (self.__chamber_pointer + 1) % self.__chambers
            return True
        return False

    # Я посчитал, что метод должен изменять передаваемый список, убирая пули из списка и добавляя их в барабан
    def add_bullets_from_list(self, lst):
        # проверяю если барабан пустой, то возвращаю False, иначе добавляю из списка пули и возвращаю True
        if len(list(filter(lambda bullet: bullet is not None, self.__bullets))) == self.__chambers:
            return False
        for i in range(self.__chambers):
            if self.__bullets[i] is None:
                self.__bullets[i] = lst.pop()
        return True

    # Немного вольности с принтами
    def shoot(self):
        if self.__bullets[self.__chamber_pointer] is None:
            print('Сlick')
            return None
        else:
            fired_bullet = self.__bullets[self.__chamber_pointer]
            self.__bullets[self.__chamber_pointer] = None
            self.__chamber_pointer = (self.__chamber_pointer + 1) % self.__chambers
            print("BANG!")
            return fired_bullet

    def unload(self, all_items=False):
        if all_items:
            bullets_to_unload = list(filter(lambda bullet: bullet is not None, self.__bullets))
            self.__bullets = [None] * self.__chambers
        else:
            bullets_to_unload = self.__bullets[self.__chamber_pointer]
            self.__bullets[self.__chamber_pointer] = None
        return bullets_to_unload

    def scrool(self):
        self.__chamber_pointer = random.randint(0, self.__chambers - 1)

    def bullet_count(self):
        return len(list(filter(lambda bullet: bullet is not None, self.__bullets)))


# проверяю созданный класс Revolver
# создаю класс Bullet
class Bullet:
    def __init__(self, coliber='.357 Magnum'):
        self.coliber = coliber


# Создаю массив с пулями
lst_of_bullets = []
for i in range(6):
    lst_of_bullets.append(Bullet())
print(lst_of_bullets)

# создаю экземпляр класса
MP_412_rex = Revolver()

# выстрел без патрона
MP_412_rex.shoot()

# добавление патронов
MP_412_rex.add_bullet(Bullet())
MP_412_rex.add_bullet(Bullet())
# Проверка количества патрон в барабане
print(MP_412_rex.bullet_count())
MP_412_rex.add_bullets_from_list(lst_of_bullets)

# ВЫСТРЕЛ
MP_412_rex.shoot()

# Извелечение патрона
MP_412_rex.unload(False)

# Извлечение всех патрон
MP_412_rex.unload(True)

# Прокрутка баробана
MP_412_rex.scrool()

