import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second...\n', end='')
    time.sleep(seconds)
    return 'Done sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executer:
    f1 = executer.submit(do_something, 1.5) # future object
    f2 = executer.submit(do_something, 1.5)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
