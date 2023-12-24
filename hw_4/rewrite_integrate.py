from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import logging
import math
import multiprocessing

from hw_4.fibonacci import count_time

LOGS_PATH = "artifacts/parallel_integrate_logs.txt"
COMPARE_PATH = "artifacts/concurrent_compare.txt"

logging.basicConfig(filename=LOGS_PATH,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger('urbanGUI')


def calculate_chunk(chunk_i, f, a, chunk_size, step):
    logger.info(f"Started computing chunk {chunk_i}.")
    chunk_result = 0
    for j in range(chunk_i, chunk_i + chunk_size):
        x = a + j * step
        chunk_result += f(x) * step
    logger.info(f"Finished computing chunk {chunk_i}.")
    return chunk_result


def parallel_integrate(f, a, b, executor, *, n_jobs=1, n_iter=1000000):
    chunk_size = n_iter // n_jobs
    step = (b - a) / n_iter

    acc = 0
    with executor:
        futures = {executor.submit(calculate_chunk, chunk_i, f, a, chunk_size, step) for chunk_i in
                   range(0, n_iter, chunk_size)}
        for future in as_completed(futures):
            acc += future.result()

    return acc


if __name__ == "__main__":
    cpu_count = multiprocessing.cpu_count()

    f = math.cos
    a = 0
    b = math.pi / 2
    results = []
    for n_jobs in range(1, cpu_count * 2 + 1):
        thread_pool_executor = ThreadPoolExecutor(max_workers=n_jobs)
        process_pool_executor = ProcessPoolExecutor(max_workers=n_jobs)

        thread_time = count_time(lambda: parallel_integrate(f, a, b, thread_pool_executor, n_jobs=n_jobs))
        process_time = count_time(lambda: parallel_integrate(f, a, b, process_pool_executor, n_jobs=n_jobs))
        results.append((n_jobs, thread_time, process_time))

    with open(COMPARE_PATH, 'w') as f:
        for n_jobs, res_thread, res_process in results:
            f.write(f"n_jobs = {n_jobs}\n")
            f.write(f"Threads result: {res_thread}\n")
            f.write(f"Process result: {res_process}\n")