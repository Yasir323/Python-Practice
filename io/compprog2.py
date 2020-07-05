import sys


def get_int():
    sys.stdout.write("Enter number(s). ")
    sys.stdout.flush()
    return map(int, sys.stdin.readline().strip().split())
# strip(): Remove spaces at the beginning and at the end of the string


def get_float():
    sys.stdout.write("Enter number(s). ")
    sys.stdout.flush()
    return map(float, sys.stdin.readline().strip().split())


def get_list_of_int():
    sys.stdout.write("Enter numbers followed by space. ")
    sys.stdout.flush()
    return list(map(int, sys.stdin.readline().strip().split()))


def get_string():
    sys.stdout.write("Enter string. ")
    sys.stdout.flush()
    return sys.stdin.readline().strip()


a, b, c, d = get_int()
e, f, g = get_float()
arr = get_list_of_int()
str = get_string()
