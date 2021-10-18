import time
import threading

start = time.perf_counter()


def do_something():
    # print('Sleeping 1 second...')
    print('Sleeping 1 second...\n', end='')
    time.sleep(1)
    # print('Done sleeping...')
    print('Done sleeping...\n',end='')


"""
When using print in a multi-threaded environment, you can
end up switching threads between those two distinct steps;
threads 1, 2 and 3 can all end up writing the printed
message first, switch threads, and only after the other
thread has written their message is the newline written.

By adding \n to your message instead, you make sure that the
newline is written at the same time. You really are writing
two newlines to sys.stdout in that case.
"""
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
