# FASTER INPUT AND OUTPUT

"""1. sys.stdin on the other hand is a
File Object. It is like creating any
other file object one could create to
read input from the file. In this case,
the file will be standard input buffer.
2. stdout.write(‘D\n’) is faster than print ‘D’.
3. Even faster is to write all once by
stdout.write(“”.join(list-comprehension))
but this makes memory usage dependent
on size of input."""

# import inbuilt standard input and output
from sys import stdin, stdout


def main():
    n = stdin.readline()
    stdout.write(str(n))
    arr = [int(x) for x in stdin.readline().split()]

    summation = 0

    for x in arr:
        summation += x

    # Or we could just use inbuilt function:
    # summation = sum(arr)

    # print answer via write which only prints strings
    # so we need to convert data into string
    stdout.write(str(summation))


# call the main method
if __name__ == "__main__":
    main()
