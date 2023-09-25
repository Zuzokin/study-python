import math


def circle(radius=5):
    area = math.pi * radius * radius
    length = math.pi * 2 * radius
    return area, length


def triangle(a=7, b=2, c=8):
    if a > b + c or b > a + c or c > a + b:
        print('Треугольника с такими сторонами не существует')
        return None
    perimeter = a + b + c
    half_p = perimeter / 2
    area = math.sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))
    return a + b + c, area


def square(side=15):
    perimeter = side * 4
    area = side * side
    return perimeter, area
