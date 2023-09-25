import random
import sys
import time
from contextlib import contextmanager


# Task 1
def divisison(expression: str):
    values = expression.split()
    try:
        return float(values[0]) / float(values[2])
    except ZeroDivisionError:
        return 'ERROR'


print(divisison('23 / 0'))


# Task 2
def passwords_validation(*passwords):
    result = []
    for password in passwords:
        try:
            int(password, 16)
            result.append(password)
        except ValueError:
            print('wrong number')
    return result


print(passwords_validation('A1', '1234MMM', '22'))

# Task 3
olympiad1 = {"name": "Пробная вышка",
             "winners": {
                 "Олеся Олимпиадникова": 594,
                 "Олег Олимпиадников": 587,
                 "Онисим Олимпиадников": 581,
             }
             }

olympiad2 = {"name": "Горные воробьи",
             "winners": {
                 "Ольга Олимпиадникова": (20, 20, 19, 20),
                 "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
                 "Офелия Олимпиадникова": (20, 20, 20, 20, 13)
             }
             }


def print_status(olympiad, participant_name):
    scores = ''
    try:
        olympiad['winners'][participant_name]  # так написано, чтобы попрактиковать исключения
        status = 'победитель'
        if olympiad['name'] == 'Горные воробьи':
            try:
                scores = olympiad["winners"][participant_name][4]
            except IndexError:
                scores = ''
        else:
            scores = olympiad["winners"][participant_name]
    except KeyError:
        status = 'призер'

    print(f'[{olympiad["name"]}] {status} {scores}')


def check_olympiad_scores(participant_name: str, *olympiads: dict):
    for olympiad in olympiads:
        print_status(olympiad, participant_name)


check_olympiad_scores('Ольга Олимпиадникова', olympiad1, olympiad2)
check_olympiad_scores('Олеся Олимпиадникова', olympiad1, olympiad2)


# Task 4
def ignorant_func(list_of_jokes):
    print('Хочешь анекдот?')
    print('...')
    input()
    print('Конечно хочешь!')
    try:
        print('Ща вспомню...\nОоо, слушай...')
        print(random.choice(list_of_jokes))
        ignorant_func(list_of_jokes)
    except KeyboardInterrupt:
        print('=' * 50)
        print('ЧТО ТЫ НАЧИНАЕШЬ, НОРМАЛЬНО ЖЕ ОБЩАЛИСЬ!!!?')
        print('=' * 50)
        time.sleep(5)
        print('Ладно, давай представим, что ты не нажимал эту кнопку')
        print('Только больше так не делай\n')
        input()
        ignorant_func(list_of_jokes)


def endless_joi():
    with open('not-funny-jokes.txt', 'r', encoding="utf-8") as joke_file:
        list_of_jokes = joke_file.read().split('\n* * *\n')
        ignorant_func(list_of_jokes)


# endless_joi()


# Task 5
class NegativeValueException(Exception):
    pass


class ZeroValueException(Exception):
    pass


class MaxValueException(Exception):
    pass


class WrongOrderException(Exception):
    pass


class PourException(Exception):
    pass


class WrongDrinksException(Exception):
    pass


class WrongContainersException(Exception):
    pass


@contextmanager
def nested_break():
    class NestedBreakException(Exception):
        pass

    try:
        yield NestedBreakException
    except NestedBreakException:
        pass


class CouldJustSaidNot(Exception):
    pass


def zahodit_testirovshik_v_bar():
    print("Заходит однажды тестировщик в бар.")
    another_one = True
    while another_one:
        drinks = ('лимонада', 'пива', 'водки', 'вина', 'воды')
        drink_endings = [['ек', 'ку', 'ки'], ['', 'ы', 'а', 'ов'], ['ку', 'ок', 'ки']]
        containers_and_endings = {'круж': drink_endings[0], 'стакан': drink_endings[1],
                                  'бокал': drink_endings[1], 'рюм': drink_endings[2]}
        print('Бармен говорит: "заказ должен выглядить так: Количество; емкость, в которой подается напиток; напиток"')
        order = input('Заказывает:').split()
        try:
            if len(order) != 3:
                raise WrongOrderException

            elif order[1] == 'в':
                raise PourException

            elif int(order[0]) < 0:
                raise NegativeValueException

            elif int(order[0]) == 0:
                raise ZeroValueException

            elif int(order[0]) > sys.maxsize:
                raise MaxValueException

            elif order[2] not in drinks:
                raise WrongDrinksException

            with nested_break() as loop_breaker:
                for drink, endings in containers_and_endings.items():
                    for end in endings:
                        if order[1] == drink + end:
                            print("Бармен начинает делать ваш заказ")
                            raise loop_breaker
                raise WrongContainersException

        except WrongOrderException:
            print('WrongOrderException')
            print('Бармен закатывает глаза и показывает тебе пальцем на табличку с правилом заказа')

        except NegativeValueException:
            print('NegativeValueException')
            print(
                'Может быть бармен и согласился взять у тебя что-то, но твоя жадность берет вверх. Ты не готов расстаться'
                ' со своим имуществом')

        except ZeroValueException:
            print('ZeroValueException')
            print('Бармен забирает у тебя 0 денег и говорит, что сейчас всё будет. Позже он наливает тебе ничего.'
                  ' Ты довольно выпиваешь ничего. Посетители начинают странно на тебя коситься')

        except MaxValueException:
            print('MaxValueException')
            print('Бармен тебе говорит: "А может ты лучше сразу купишь весь бар?"')

        except WrongDrinksException:
            print('WrongDrinksException')
            print('У нас мы такое не продаем')
        except WrongContainersException:
            print('WrongContainersException')
            print('Мы в такое не наливаем')
        except PourException:
            print('PourException')
            print('Мы ничего никуда не засовываем, не подсыпываем, не мешаем и т.п.')
        finally:
            answer = input('еще по одной?(y,n >>>')
            try:
                if answer == 'y':
                    print("What's the spirit")

                elif answer == 'n':
                    print('Нет, так нет')
                    another_one = False

                assert (answer == 'y' or answer == 'n')
            except AssertionError:
                print('мог бы просто сказать нет')
                another_one = False


zahodit_testirovshik_v_bar()
