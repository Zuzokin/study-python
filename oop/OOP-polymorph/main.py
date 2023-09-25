from abc import ABC, abstractmethod


# region Task 1
class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


class Autobiography(Book):
    def display(self):
        print(f'{self.title}- прекрасная книга, написанная в автобиографическом жанре. Автор - {self.author}\n')


class Psychology(Book):
    def display(self):
        print(f'{self.title}- прекрасная книга, написанная в жанре психологии. Автор - {self.author}\n')


class Fantasy(Book):
    def display(self):
        print(f'{self.title}- прекрасная книга, написанная в жанре фэнтези. Автор - {self.author}\n')


book1 = Autobiography('К черту все! Берись и делай!', 'Ричард Брэнсон')
book2 = Psychology('Биология добра и зла', 'Роберт Сапольски')
book3 = Fantasy('Песнь льда и пламени', 'Джордж Реймонд Ричард Мартин')

book1.display()
book2.display()
book3.display()


# endregion

# region Task 2
class Bird:
    def feed(self):
        print('Feeding bread crumbs')


class Swan(Bird):
    def feed(self):
        print('Feeding the swan bread crumbs')


class Duck(Bird):
    def feed(self):
        print('Feeding the duck bread crumbs')


class Animal(ABC):
    @abstractmethod
    def feed(self):
        pass


class Mouse(Animal):
    def feed(self):
        print('Feeding the mouse bread crumbs')


def feed(bird: Bird | Animal):
    bird.feed()


feed(Duck())
feed(Mouse())

# endregion

# region Task 3
print('-' * 50)


class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question: str = 'Как какать?'):
        print('Очень интересный вопрос! Давайте разбираться вместе!')


class Student(Human):
    def ask_question(self, percon: Human, question: str):
        print(f'{percon.name}, {question}')
        percon.answer_question(question)


class Teacher(Human):
    def answer_question(self, question: str = 'Как какать?'):
        if question == "как войти в айти?":
            print('Можешь начать осваивать программирование с ППШ')
        elif question == 'как научится программировать?':
            print('Сейчас расскажу')
        else:
            super().answer_question(question)


class Mentor(Human):
    def answer_question(self, question: str = 'Как какать?'):
        if question == "как повысить эффективность работы?":
            print('Важно соблюдать три правила')
        elif question == 'как додуматься до этого решения?':
            print('Сейчас опишу ход мыслей при решении задачи')
        else:
            super().answer_question(question)
            # self.answer_question(question)


class CodeReviewer(Human):
    def answer_question(self, question: str = 'Как какать?'):
        if question == "я усовершенствовал свой код. Вы проверите?":
            print('Замечательный вариант решения. Вы отлично справились!')
        else:
            self.answer_question(question)


class Curator(Human):
    def answer_question(self, question: str = 'Как какать?'):
        if question == "как додуматься до этого решения?":
            print('Можешь начать осваивать программирование с ППШ')
        else:
            self.answer_question(question)


student1 = Student('Ваня')
teacher = Teacher('Александр Романович')
mentor1 = Mentor('Илья')
curator1 = Curator('Владимир')
reviewer1 = CodeReviewer('Евгений')

student1.ask_question(teacher, 'как войти в айти?')
student1.ask_question(teacher, 'как научится программировать?')
student1.ask_question(mentor1, 'как повысить эффективность работы?')
student1.ask_question(curator1, 'как додуматься до этого решения?')
student1.ask_question(reviewer1, 'я усовершенствовал свой код. Вы проверите?')
# endregion

# region Task 4
print('-' * 50)


class GeometricFigures(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass


class Triangle(GeometricFigures):
    def __init__(self, sideA, sideB, sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def __str__(self):
        return f'Треугольник со сторонами {self.sideA}, {self.sideB}, {self.sideC}.'

    def get_perimeter(self):
        return f'Периметр равен: {self.sideA + self.sideB + self.sideC}'


class Square(GeometricFigures):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Квадрат со стороной {self.side}.'

    def get_perimeter(self):
        return f'Периметр равен: {self.side * 4}'


class Rectangle(GeometricFigures):
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def __str__(self):
        return f'Прямоугольник со сторонами {self.sideA} {self.sideB}'

    def get_perimeter(self):
        return f'Периметр равен: {self.sideA * 2 + self.sideA * 2}'


figures = [Triangle(1, 2, 3), Triangle(4, 5, 6),
           Square(10), Square(20),
           Rectangle(6, 7), Rectangle(7, 8)]

for figure in figures:
    print(figure, figure.get_perimeter())

# endregion

# region Task 5
print('-' * 50)


class Command(ABC):
    @abstractmethod
    def vote_command(self):
        pass

    @abstractmethod
    def gesture_command(self):
        pass


class Lock(ABC):
    @abstractmethod
    def close_lock(self):
        pass

    @abstractmethod
    def open_lock(self):
        pass


class SmartAssistant(Command):
    def vote_command(self):
        print('Умный помощник распознал голосовую команду')

    def gesture_command(self):
        print('Умный помощник распознал жестовые команды')

    def open_lock(self):
        raise NotImplementedError('Извините, я не могу это сделать')

    def close_lock(self):
        raise NotImplementedError('Извините, я не могу это сделать')


class SmartCamera(Command, Lock):
    def vote_command(self):
        print('Умная камера распознала голосовую команду')

    def gesture_command(self):
        print('Умная камера распознала жестовые команды')

    def open_lock(self):
        print('Умная камера открыла замок входной двери')

    def close_lock(self):
        print('Умная камера закрыла замок входной двери')


class SmartLock(Lock):
    def open_lock(self):
        print('Умный замок открыл входную дверь')

    def close_lock(self):
        print('Умный замок закрыл входную дверь')

    def vote_command(self):
        raise NotImplementedError('Извините, я не могу это сделать')

    def gesture_command(self):
        raise NotImplementedError('Извините, я не могу это сделать')


sa = SmartAssistant()
sa.vote_command()
sa.gesture_command()

sc = SmartCamera()
sc.open_lock()
sc.close_lock()
sc.vote_command()
sc.gesture_command()

sl = SmartLock()
sl.open_lock()
sl.close_lock()

# endregion