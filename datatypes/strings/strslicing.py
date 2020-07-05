def check(input, pattern):
    if len(input) == 0 and len(pattern) == 0:
        return False

    if len(pattern) == 0:
        return False

    while(len(input) == 0):
        # FIND METHOD FINDS THE "PATTERN" IN THE "INPUT" STRING
        # AND RETURNS THE INDEX
        index = input.find(pattern)
        if index == -1:
            return False

        input = input[0:index] + input[(index + len(pattern)):]

    return True


# Driver program
def main():
    input = "GeeGeeksks"
    pattern = "Geeks"
    print(check(input, pattern))


if __name__ == "__main__":
    main()
