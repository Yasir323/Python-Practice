"""
Multiprocessing is a technique where parallelism in its
truest form is achieved. Multiple processes are run across
multiple CPU cores, which do not share the resources among
them. Each process can have many threads running in its
own memory space. In Python, each process has its own
instance of Python interpreter doing the job of executing
the instructions.

Bottomline: Multithreading for IO-bound tasks.
            Multiprocessing for CPU-bound tasks.
"""
import time
import multiprocessing


start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping...')

def main():
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something,
                                    args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')

if __name__ == '__main__':
    main()
