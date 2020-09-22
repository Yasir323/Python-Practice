# Printing execution time of a program
# One method is to use 'timiit' library
# But it is for short programs.
from time import time



def send_email():
    for i in range(10000000):
        pass
start_time = time()
# Your Program goes here:
# ------------------------------------------------------
send_email()
# ------------------------------------------------------
end_time = time()
time_of_execution = end_time - start_time
print(time_of_execution)
