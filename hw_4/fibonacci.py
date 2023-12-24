import time
from threading import Thread
from multiprocessing import Process


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


NUMBER_OF_BENCH_RUNS = 10


def count_time(lambd):
    start = time.time()
    lambd()
    finish = time.time()
    return finish - start


def count_synchronous_time(inner_lambd):
    def lambd():
        for i in range(NUMBER_OF_BENCH_RUNS):
            inner_lambd()

    return count_time(lambd)


def count_threads_time(inner_lambd):
    def lambd():
        threads = []
        for _ in range(NUMBER_OF_BENCH_RUNS):
            t = Thread(target=inner_lambd)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    return count_time(lambd)


def count_multiprocessing_time(inner_lambd):
    def lamd():
        procs = []
        for _ in range(10):
            p = Process(target=inner_lambd)
            p.start()
            procs.append(p)

        for p in procs:
            p.join()

    return count_time(lamd)


if __name__ == "__main__":
    results_file_path = "artifacts/count_fibonacci_time.txt"

    bin_g_value = 35
    inner_lambd = lambda: fibonacci(bin_g_value)

    synchronous_time = count_synchronous_time(inner_lambd)
    threads_time = count_threads_time(inner_lambd)
    multiprocessing_time = count_multiprocessing_time(inner_lambd)
    with open(results_file_path, 'w') as f:
        f.write(f"Synchronous time:     {synchronous_time}\n")
        f.write(f"Threads time:         {threads_time}\n")
        f.write(f"Multiprocessing time: {multiprocessing_time}\n")
