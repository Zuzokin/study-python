import time
import os
import multiprocessing
from multiprocessing import Process
from random import randint
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        execution_time = end - start
        print(
            f"Function {func.__name__}{args} {kwargs} with result {result} Took {execution_time:.4f} seconds"
        )
        return result

    return wrapper


def generate_file(file_size=1):
    with open("file.txt", "w") as f_o:
        for _ in range(file_size):
            f_o.write(f"{randint(0, 9)}\n")


@timeit
def calc_smth(*mock_args, **mock_kwargs):  # mock_args нужны для pool
    result = 0
    with open("file.txt", "r") as f_o:
        for s in f_o:
            result += randint(0, int(s))
    print(f"result = {result}, pid = {os.getpid()}")
    return result


@timeit
def read_something():
    with open("file.txt", "r") as f:
        for s in f:
            pass


@timeit
def calc_smth_twice():
    calc_smth()
    calc_smth()


@timeit
def calc_smth_twice_with_process():
    p = Process(target=calc_smth)
    p_1 = Process(target=calc_smth)
    p.start()
    p_1.start()
    p.join()
    p_1.join()


@timeit
def calc_smth_twice_with_process_refactor():
    p_list = [Process(target=calc_smth) for _ in range(2)]
    [p.start() for p in p_list]
    # без этого основной поток слишком быстро завершит работу, но это не помешает дочерним
    [p.join() for p in p_list]


@timeit
def calc_smth_pool():
    with multiprocessing.Pool(2) as pool:
        pool.map(calc_smth, range(2))  # нужны mock args


if __name__ == "__main__":
    calc_smth_pool()
    calc_smth_twice_with_process_refactor()
    calc_smth_twice_with_process()
    calc_smth_twice()
