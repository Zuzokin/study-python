# Задача 2
def compare_passwords():
    print('Введите пароль')
    password = input()
    print('Введите пароль еще раз')
    password_to_compare = input()
    print(password == password_to_compare)

# compare_passwords()


# Задача 3
def min_number_of_four():
    print('Введите 1ое число')
    a = int(input())
    print('Введите 2ое число')
    b = int(input())
    print('Введите 3е число')
    c = int(input())
    print('Введите 4ое число')
    d = int(input())
    print(min(a, b, c, d))


# min_number_of_four()


# Задача 4
def max_number_of_four():
    print('Введите 1ое число')
    a = int(input())
    print('Введите 2ое число')
    b = int(input())
    print('Введите 3е число')
    c = int(input())
    print('Введите 4ое число')
    d = int(input())
    print(max(a, b, c, d))


# max_number_of_four()


# Задача 5
def is_triangle_exist():
    print('Введите длину 1ой стороны')
    a = int(input())
    print('Введите длину 2ой стороны')
    b = int(input())
    print('Введите длину 3ей стороны')
    c = int(input())
    # Если каждая сторона треугольника меньше суммы двух других сторон, значит треугольник существует.
    print((a < b + c) and (b < a + c) and (c < a + b))


# is_triangle_exist()


# Задача 6
def type_of_triangle():
    print('Введите длину 1ой стороны')
    a = int(input())
    print('Введите длину 2ой стороны')
    b = int(input())
    print('Введите длину 3ей стороны')
    c = int(input())
    first_sign_of_exist = (a <= b + c) and (b <= a + c) and (c <= a + b)
    if (a <= 0) or (b <= 0) or (c <= 0) or not first_sign_of_exist:
        print('Треугольник не существует')
    elif a == (b + c) or b == (a + c) or c == (a + b):
        print('Треугольник вырожденный')
    elif a == b and a == c:
        print('Треугольник равносторонний')
    elif a != b and a != c:
        print('Треугольник разносторонний')
    else:  # Возможно здесь стоило написать проверку, но вроде все случаи я учел и оно работает :)
        print('Треугольник равнобедренный')


# type_of_triangle()


# Задача 7
def quantity_of_intersecting_points():
    print('Введите a')
    a = int(input())
    print('Введите b')
    b = int(input())
    print('Введите c')
    c = int(input())
    print('Введите d')
    d = int(input())

    # Делаю введенные данные удобными для работы, если их ввел капибара
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if a > c:
        a, b, c, d = c, d, a, b
    print(f'Вы ввели отрезки:[{a}, {b}], [{c}, {d}]')

    if b < c:  # нет пересекаются
        print(0)
    elif d < b:  # один отрезок полностю в внутри другого
        print(d - c + 1)
    else:  # отрезки пересекаются частично или совпадают
        print(b - c + 1)

quantity_of_intersecting_points()
