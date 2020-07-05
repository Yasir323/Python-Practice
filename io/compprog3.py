"""
1. Simply, adding the buffered IO code before
your submission code to make the output faster.

2. The benefit of io.BytesIO objects is that they
implement a common-ish interface (commonly known
as a ‘file-like’ object). BytesIO objects have an
internal pointer and for every call to read(n)
the pointer advances.

3. The atexit module provides a simple interface
to register functions to be called when a program
closes down normally. The sys module also provides
a hook, sys.exitfunc, but only one function can be
registered there. The atexit registry can be used
by multiple modules and libraries simultaneously.
"""


# template begins
#####################################

# import libraries for input/ output handling
# on generic level
import atexit, io, sys

# A stream implementation using an in-memory bytes
# buffer. It inherits BufferedIOBase.
buffer = io.BytesIO()
sys.stdout = buffer


# print via here
# atexit decorator call a function who gets
# the value from 'buffer' object and write
# it to sys.__stdout__ object (who will
# print in console) when the script ends
@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue().decode() + '\n')


#####################################
# template ends

# normal method followed
# input N
n = int(input())

# input the array
arr = [int(x) for x in input().split()]

# initialize variable
summation = 0

# calculate sum
for x in arr:
    summation += x

# 'summation' is casted to bytes before writing
# itself in the 'buffer' object besides, it
# must be casted to 'string' before that
summation = str(summation).encode()
buffer.write(summation)
