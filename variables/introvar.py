'''
In Python, value of an integer is not restricted by the
number of bits and can expand to the limit of the
available memory.

Computations with integers are exact, whereas those that
involve floating point numbers are not. The accuracy of
a floating point computation depends on the precision
of the numbers used. Greater the precision, the more
accurate the result. But there is limit to the precision
of floating numbers. The precision is limited to the
number of bits used. 32-bit floating point numbers have
lower precision than 64-bit numbers. There is also a
limit to how big or how small a floating point number
you can represent. For a 32-bit representation the range
is (+/-) 3.4E38 and for 64-bit representation the range
is (+/-) 1.8E308.

There is also a limit to the range of integers that you
can represent. With 32 bits the range is -231 to (231 - 1).
In mixed operations, those that involve both integers
and floating numbers, integers are converted to floating
point numbers and the computation performed. Careful:
consider this expression: 3.5 + (6/4). The result is
4.5 and not 5.0
'''
