import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second...\n', end='')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)'


with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [5, 4, 3, 2, 1]
    future_objects = [executer.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(future_objects):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
