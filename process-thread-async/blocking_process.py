import time
from multiprocessing import Process, Lock, RLock
from random import random


def file_writer(start, finish):
    with open("locker.txt", "a") as f_o:
        for i in range(start, finish):
            time.sleep(
                random()
            )  # несмотря на random и консоль всё ок; PS семафор постарался, вызвав блокировку
            print(i)
            f_o.write(f"{i}\n")


def file_writer_shaffle(start, finish):
    # меняю местами with и for
    for i in range(start, finish):
        with open("locker.txt", "a") as f_o:
            time.sleep(random())
            print(i)
            f_o.write(f"{i}\n")
            # здесь срабатывает __exit__ и семафор не работает


def file_writer_with_Rlocker(start: int, finish: int, locker: Lock):
    locker.acquire()
    for i in range(start, finish):
        with open("locker.txt", "a") as f_o:
            time.sleep(random())
            print(i)
            f_o.write(f"{i}\n")
    # для безопасности процессов, чтобы другой процесс не снял блокировку - Rlock
    p = Process(target=releaser,
                args=(locker,))
    p.start()


def releaser(locker: Lock):
    print("Какая-то полезная работа при релизе")
    locker.release()


def write_in_file_without_lock(func):
    p1 = Process(target=func, args=(0, 5))
    p2 = Process(target=func, args=(5, 10))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def write_in_file_with_lock(func):
    lock = RLock()
    p1 = Process(target=func, args=(0, 5, lock))
    p2 = Process(target=func, args=(5, 10, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    write_in_file_with_lock(file_writer_with_Rlocker)
