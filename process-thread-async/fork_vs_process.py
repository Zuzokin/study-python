import time
import os
from multiprocessing import Process
from datetime import datetime

CNT = 0


# region fork functions
def create_with_fork_child_process():
    print(f"Начинаю работу в процессе {os.getpid()}")
    res = os.fork()
    print(res, os.getpid())
    # if res == 0 значит мы в дочернем процессе, иначе в родительском


def create_with_fork_processes_in_for_loop(num_fork):
    # --- and *** for easier calculation
    # print(f"---Начинаю работу в процессе {os.getpid()}")

    for i in range(num_fork):
        pid_marker = os.fork()
        if pid_marker != 0:
            print(
                f"---Порождаю дочерний процесс {pid_marker} из процесса {os.getpid()}"
            )
    print(f"***Продолжаю работу в процессе {os.getpid()}")


# endregion


# region multiprocessing functions
def some_function(sleep_time=3):
    global CNT
    print(f"function started from", os.getpid())
    time.sleep(sleep_time)
    CNT += 1
    print(f"function finished with {CNT} from", os.getpid())


# Недостатки порождения процессов:
# 1. высокие накладные расходы, за счет того, что под капотом нужно будет заводить новый интерпретатор
# и подгружать туда заново все исполняемые модули
#
# 2. процессы имеют изолированные области памяти, поэтому для общения между ними придётся изобретать костыли


def create_processes_with_multiprocessing():
    global CNT
    p = Process(target=some_function, args=(5,))
    p_1 = Process(target=some_function, args=(10,))
    print(p)

    p.start()
    print(p)

    p_1.start()
    # нужна синхронизация, тк выполнение дочерних процессов дольше, чем родительского
    p.join()
    p_1.join()

    print("final value:", CNT)  # У процессов независимые участки памяти


# endregion


if __name__ == "__main__":
    create_with_fork_child_process()
    print("-" * 50)
    create_with_fork_processes_in_for_loop(2)
    print("-" * 50)
    create_processes_with_multiprocessing()
