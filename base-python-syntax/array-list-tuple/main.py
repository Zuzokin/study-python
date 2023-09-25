# Задача 3
def calc_arithmetic_mean():
    n = int(input())
    sequence = []
    for i in range(n):
        number = int(input())
        sequence = sequence + [number]
    print(sum(sequence) / n)


# calc_arithmetic_mean()


# Задача 4
def find_elem():
    n = int(input())
    m = int(input())
    sequence = []
    for i in range(n):
        number = int(input())
        sequence = sequence + [number]
    print(sequence[m])


# find_elem()

# Задача 5
def find_even_elem_sum():
    n = int(input())
    sequence = []
    for i in range(n):
        number = int(input())
        sequence = sequence + [number]
    result = 0
    for i in range(0, n, 2):
        result = result + sequence[i]
    print(result)

# find_even_elem_sum()
