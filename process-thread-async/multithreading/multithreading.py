from threading import Thread
import threading
import os
from functools import wraps
import time
from concurrent.futures import ThreadPoolExecutor

CNT = 0


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


def func_inc_global_cnt():
    global CNT
    for _ in range(1_000_000):
        CNT += 1
    print(
        f"Это поток {threading.get_ident()} из процесса {os.getpid()} с результатом {CNT}"
    )


def func_sleep():
    """Функция с имитацией I/O операций"""
    print(f"Это поток {threading.get_ident()} из процесса {os.getpid()}")
    time.sleep(1)


def func_heavy_math():
    """Функция с тяжелыми вычислениями"""
    cnt = 0
    for _ in range(50_000_000):
        cnt += 1
    print(f"Это поток {threading.get_ident()} из процесса {os.getpid()}")


@timeit
def synchron(func):
    [func() for _ in range(3)]


@timeit
def async_threading(func):
    th_list = [Thread(target=func) for _ in range(3)]
    [th.start() for th in th_list]
    [th.join() for th in th_list]


@timeit
def pool_executor(func, workers_quantity):
    with ThreadPoolExecutor(max_workers=workers_quantity) as t:
        [t.submit(func) for _ in range(workers_quantity)]


if __name__ == "__main__":
    synchron(func_sleep)
    async_threading(func_sleep)
    synchron(func_heavy_math)
    async_threading(func_heavy_math)
    pool_executor(func_inc_global_cnt, 10)
