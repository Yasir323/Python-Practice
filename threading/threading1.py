"""
When multiple processes(threads) are running on a CPU core
and one process takes awful lot of time for executing an I/O
bound task, we can use MultiThreading to avoid waiting for that
thread to complete and perform some other task in the mean time.
This shouldn't be done when the Thread is performing an
extensive CPU bound process. It will increase the time of execution.

Multithreading is a technique where multiple threads are
spawned by a process to do different tasks, at about the
same time, just one after the other. This gives you the
illusion that the threads are running in parallel, but
they are actually run in a concurrent manner. In Python,
the Global Interpreter Lock (GIL) prevents the threads
from running simultaneously.
"""
import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
