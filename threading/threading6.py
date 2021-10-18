import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second...\n', end='')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)'


with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [5, 4, 3, 2, 1]
    results = executer.map(do_something, secs) # result object
    for result in results:
        print(result)
# map returns the function in the order they were executed.

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
