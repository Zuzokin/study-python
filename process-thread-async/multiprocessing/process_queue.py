from multiprocessing import Queue, Pipe, Process
from queue import Empty
from time import sleep
from typing import List


def worker(a: int, q: Queue):
    cnt = 0
    while cnt < a:
        sleep(0.3)  # какое-то вычисление
        q.put(cnt)
        cnt += 1
    print("W1 ended!")


def worker2(a: int, q: Queue):
    cnt = 0
    while cnt < a:
        sleep(0.1)
        cnt += 1
    print("snatch", q.get())
    print("put new value", 123321)
    q.put(123321)


def pipe_worker(p: Pipe, data):
    some_data = data * 2
    p.send(some_data)


def pipe_worker2(p: Pipe):
    print("pw2", (p.recv()))


def basic_queue():
    q = Queue()
    p = Process(target=worker, args=(3, q))
    p.start()
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get(timeout=1))
    p.join()


def queue_error_handler():
    q = Queue()
    p = Process(target=worker, args=(3, q))
    p.start()
    p1 = Process(target=worker2, args=(3, q))
    p1.start()
    sleep(1)
    print("get values from queue")
    try:
        for _ in range(10):
            print(q.get(timeout=1))
    except Empty as err:
        print("Empty queue", err)
    p.join()
    p1.join()


def pipe_example():
    # с одного конца впихиваем данные, с другого читаем если duplex = FALSE
    parent_pipe, child_pipe = Pipe(duplex=True)
    p = Process(target=pipe_worker, args=(child_pipe, 123))
    p.start()
    p1 = Process(target=pipe_worker2, args=(child_pipe,))
    p1.start()
    print("Информация из дочернего процесса:", parent_pipe.recv())
    parent_pipe.send("Информация из главного процесса")
    p.join()
    p1.join()


if __name__ == "__main__":
    pass
