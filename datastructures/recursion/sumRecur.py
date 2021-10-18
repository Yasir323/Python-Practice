def sum_of_digits(num):
    # Unintentional case
    assert num >= 0 and int(num) == num, "The number has to be \
     a postive integer only."

    # Base case
    if num == 0:
        return 0
    # Recursive case
    else:
        return int(num % 10) + sum_of_digits(int(num / 10))


print(sum_of_digits(112))
