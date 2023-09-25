from datetime import datetime
import datetime


# region Task 1
class HeavenlyBody:
    """Родительский класс HeavenlyBody"""

    def __init__(self, name, age, temperature, radius):
        self.radius = radius
        self.temperature = temperature
        self.age = age
        self.name = name

    def display(self):
        print(
            f'Название: {self.name}\n'
            f'Возраст: {self.age} (млн. лет)\n'
            f'Температура: {self.temperature} (С)\n' 
            f'Радиус: {self.radius} (км)'
        )


class Planet(HeavenlyBody):
    """Дочерний класс Planet"""

    def __init__(self, name, age, temperature, radius, orbital_speed):
        super().__init__(name, age, temperature, radius)
        self.orbital_speed = orbital_speed

    def display(self):
        print(
            f'Название: {self.name}\n'
            f'Возраст: {self.age} (млн. лет)\n'
            f'Температура: {self.temperature} (С)\n'
            f'Радиус: {self.radius} (км)\n'
            f'Орбитальная скорость: {self.orbital_speed} (км/с) '
        )


class Star(HeavenlyBody):
    """Дочерний класс Star"""

    def __init__(self, name, age, temperature, radius, constellation):
        super().__init__(name, age, temperature, radius)
        self.constellation = constellation

    def display(self):
        print(
            f'Название: {self.name}\n'
            f'Возраст: {self.age} (млн. лет)\n'
            f'Температура: {self.temperature} (С)\n'
            f'Радиус: {self.radius} (км)\n'
            f'Созвездие: {self.constellation}'
        )


planet1 = Planet('Земля', 4540, '16.92', 6371, '29.8')
star1 = Star('Полярная звезда', 60, '5500', 47, 'Малая Медведица')

print(Planet.__doc__, end='\n')
planet1.display()

print(Star.__doc__, end='\n')
star1.display()

# endregion

# region Task 2
print('-' * 50)


class Pastery:
    def __init__(self, name: str, price: int, manufacture_date: datetime, term: int):
        self.id = id(self)
        self.term = term
        self.manufacture_date = manufacture_date
        self.price = price
        self.name = name

    def display(self) -> None:
        print(f'Название: {self.name}')
        print(f'Цена: {self.price} (руб.)')
        print(f'Дата изготовления: {self.manufacture_date}')

    def valid_until(self) -> str:
        remaining_days = (self.manufacture_date + datetime.timedelta(days=self.term)).day - datetime.datetime.now().day
        if remaining_days < 0:
            return 'Срок годности истек'
        else:
            return f'Срок годности истекает через {remaining_days} дня'


class Cake(Pastery):
    def __init__(self, name: str, price: int, manufacture_date: datetime, term: int, filling: str):
        self.id = id(self)
        super().__init__(name, price, manufacture_date, term)
        self.filling = filling

    def order(self):
        self.display()
        f'Начинка: {self.filling}'
        # Не уверен, что это хороший код и возможно лучше использовать обычный if
        # print(
        #     f'Оформлен заказ {self.id} - {self.name} c {self.filling}'
        #     if not self.valid_until() == 'Срок годности истек'
        #     else self.valid_until()
        # )
        if self.valid_until() == 'Срок годности истек':
            print('Выберите другой торт')
        else:
            print(f'{self.valid_until()}\n'
                  f'Оформлен заказ {self.id} - {self.name} c {self.filling}')


class BentoCake(Pastery):
    def __init__(self, name: str, price: int, manufacture_date: datetime, term: int, celebration: str):
        super().__init__(name, price, manufacture_date, term)
        self.celebration = celebration

    def order(self):
        self.display()
        print(f'Праздник: {self.celebration}')
        if self.valid_until() == 'Срок годности истек':
            print('Выберите другой торт')
        else:
            print(f'{self.valid_until()}\n'
                  f'Оформлен заказ {self.id} - {self.name} на {self.celebration}')


cake1 = Cake('Торт', 1300, datetime.date(2023, 8, 25), 3, 'вишня')
bento1 = BentoCake('Бенто торт', 1000, datetime.date(2023, 7, 20),
                   4, 'день рождения')

cake1.order()
bento1.order()

# endregion

# region Task 3
print('-' * 50)


class BankAccount:
    def __init__(self, holder: str, balance: int, interest_rate: float):
        self.__holder = holder
        self._balance = balance
        self._interest_rate = interest_rate

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, new_holder):
        self.__holder = new_holder

    def __str__(self):
        print(f'Владелец: {self.holder}\n'
              f'Баланс: ${self._balance:,.2f}\n'
              f'Процентная ставка: {self._interest_rate}'
              )


class BankOperation(BankAccount):
    def __init__(self, holder: str, balance: int, interest_rate: float, operations_history: list = None):
        super().__init__(holder, balance, interest_rate)
        self.__id = id(self)
        self.__operations_history = [] if operations_history is None else operations_history

    def deposit(self, amount):
        self.__operations_history.append(f'Аккаунт {self.__id} - внесение наличных на счет: ${amount:,.2f}')
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self.__operations_history.append(f'Аккаунт {self.__id} - cнятие наличных: ${amount:,.2f}')
            self._balance -= amount
        else:
            self.__operations_history.append(f'Аккаунт {self.__id} - попытка снятия наличных: ${amount:,.2f}')
            # '\nПричина: недостаточно средств на счете'
            print('Недостаточно средств на счете')

    def add_interest(self):
        interest = self._balance * self._interest_rate
        self.__operations_history.append(f'Аккаунт {self.__id} - начислены проценты по вкладу: ${interest:,.2f}')
        self._balance += interest

    def history(self):
        print(*self.__operations_history, sep='\n')


account = BankOperation('Warren Buffett', 113000000000, 0.08)

account.__str__()
account.deposit(4000000000)
account.withdraw(88000000000)
account.withdraw(113000000001)
account.add_interest()
account.history()

# endregion

# region Task 4
print('-' * 50)


class ComputerDevice:
    """Request process"""

    def __init__(self, inf):
        print('Start init ComputerDevice.__init__()')
        self.inf = inf
        print('End init ComputerDevice.__init__()')


class Scanner(ComputerDevice):
    """Scan information"""

    def __init__(self, inf):
        print('Start init Scanner.__init__()')
        super().__init__(inf)
        print('End init Scanner.__init__()')


class Printer(ComputerDevice):
    """Print information"""

    def __init__(self, inf):
        print('Start init Printer.__init__()')
        super().__init__(inf)
        print('End init Printer.__init__()')


class Copier(Scanner, Printer):
    """Copy process"""

    def __init__(self, inf):
        print('Start init Copier.__init__()')
        super().__init__(inf)
        print(f'Отсканированная информация: {self.inf.upper()}')
        print('End init Copier.__init__()')


print(Copier.__mro__)

c = Copier('Hello world!')

# endregion

# region Task 5
print('-' * 50)


class Investments:
    def __init__(self, ticker, price, currency, industry):
        self.ticker = ticker
        self.price = price
        self.currency = currency
        self.industry = industry

    def display(self):
        print(
            f'Тикер: {self.ticker}\n'
            f'Цена: {self.price}\n'
            f'Валюта: {self.currency}\n'
            f'Сектор: {self.industry}\n'
        )

    @staticmethod
    def buying_securities(func):
        def _wrapper(security, *args, **kwargs):
            if security.echelon == 3:
                print('Это высокорискованная сделка\n')
                return None
            return func(security, *args, **kwargs)

        return _wrapper


class Shares(Investments):
    def __init__(self, ticker, price, currency, industry, dividend, echelon, profit):
        super().__init__(ticker, price, currency, industry)
        self.dividend = dividend
        self.echelon = echelon
        self.profit = profit

    @Investments.buying_securities
    def buying(self, quantity):
        if self.profit < 5:
            print('Это высокорискованная сделка\n')
            return None
        print(
            f'Совершена покупка {quantity} акций на сумму: {quantity * self.price}.\n'
            f'Поздравляю, Вы стали совладельцем компании!\n')


class Bonds(Investments):
    def __init__(self, ticker, price, currency, industry, coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry)
        self.coupon = coupon
        self.echelon = echelon
        self.nominal = nominal

    @Investments.buying_securities
    def buying(self, quantity: int):
        if self.price > self.nominal:
            print('Это высокорискованная сделка\n')
            return None
        print(f'Совершена покупка {quantity} облигаций на сумму: {quantity * self.price}.')
        if 'ОФЗ' in self.ticker:
            print(f'Поздравляю, Вы стали кредитором государства!\n')
        else:
            print('Поздравляю, Вы стали кредитором компании!\n')


i1 = Shares('GAZP', 174, 'RUB', 'Энергетика', True, 3, 6)
i1.display()
i1.buying(15)
i2 = Bonds('ОФЗ-26233', 688, 'RUB', 'Государственные', 6, 1, 1000)
i2.display()
i2.buying(5)

# endregion
