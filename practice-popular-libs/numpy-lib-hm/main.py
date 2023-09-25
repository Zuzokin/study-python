import numpy as np
from collections import Counter
from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result

    return timeit_wrapper


# region Task1

def max_col_values(arr):
    return np.max(arr, axis=0)


arr = np.array([[4, 2, 7],
                [9, 5, 1],
                [3, 8, 6]])

max_values = max_col_values(arr)


# endregion

# region Task2
def mean_grade(arr):
    return np.mean(arr, axis=1)


arr = np.array([[8, 7, 9],
                [6, 8, 7],
                [9, 9, 8],
                [7, 6, 8]])

average_grades = mean_grade(arr)


# endregion

# region Task3
def total_sales_in_each_store(arr):
    return np.sum(arr, axis=1)


arr = np.array([[10, 15, 20],
                [5, 25, 15],
                [30, 10, 5]])

total_sales = total_sales_in_each_store(arr)


# endregion

# region Task4
@timeit
def most_frequent_value_for_positive_int(arr):
    x = np.bincount(arr)
    return np.argmax(x, 0)


@timeit
def most_frequent_value(arr):
    max_value = Counter(values)
    most_frequent = max_value.most_common(1)
    return most_frequent[0][0]


@timeit
def most_frequent_value_ver2(arr):
    vals, counts = np.unique(arr, return_counts=True)
    return vals[np.argmax(counts, 0)]


from scipy import stats


@timeit
def most_frequent_value_ver3(arr):
    return stats.mode(arr)[0]


values = np.random.randint(100, size=100000)

# arr = np.random.rand(5)
arr_positive = np.array([1, 1, 2, 1, 4, 4, 4])
print(most_frequent_value_for_positive_int(values))
print(most_frequent_value(values))
print(most_frequent_value_ver2(values))
print(most_frequent_value_ver3(values))

# endregion

# region Task5
import time


# O(N+N)
@timeit
def find_lowest_point(arr):
    vals, counts = np.unique(arr, return_counts=True)
    low_p_ind = np.argmin(vals)
    return vals[low_p_ind], counts[low_p_ind]


# Faster (O(N + N(len of unique val))
@timeit
def find_lowest_point2(arr):
    lowest_point = np.min(arr)
    freq = np.count_nonzero(arr == lowest_point)
    return lowest_point, freq


array = np.random.randn(1000, 1000)

# array = np.array([[5, 4, 3],
#                   [2, 1, 1],
#                   [3, 3, 3]])

print(find_lowest_point(array))
print(find_lowest_point2(array))


# endregion

# region Task6
def validate_magic_square(array):
    is_magic_square = True

    rows_num = np.shape(array)[0]
    col_num = np.shape(array)[1]

    if rows_num != col_num:
        print('Введен не квадрат!')
        return False

    rows_sums = np.sum(array, axis=1)
    col_sums = np.sum(array, axis=0)

    diagonal = np.trace(array)
    anti_diagonal = np.trace(np.fliplr(array))

    if np.unique(rows_sums).size != 1:
        print('Суммы в рядах не равны')
        is_magic_square = False

    if np.unique(col_sums).size != 1:
        print('Суммы в столбцах не равны')
        is_magic_square = False

    if diagonal != anti_diagonal:
        print('Главная и побочные диагонали не равны')
        is_magic_square = False

    if not (diagonal == anti_diagonal == col_sums[0] == rows_sums[0]):
        print('Сумма каждой строки, столбца и диагоналей не равны')
        is_magic_square = False

    return is_magic_square


arr1 = np.array([[2, 7, 6],
                 [9, 5, 1],
                 [4, 3, 8]])

arr2 = np.array([[16, 2, 7, 9],
                 [3, 13, 12, 6],
                 [10, 8, 1, 15],
                 [5, 11, 14, 4]])

print(validate_magic_square(arr1))
print(validate_magic_square(arr2))

# endregion
