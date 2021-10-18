# Decimal to Binary conversion
binary = []


def decimal_to_binary(n):
    # Unintentionacase case
    # Base case
    if n == 0:
        pass
    # Recursive case
    else:
        binary.append(str(n % 2))
        decimal_to_binary(int(n / 2))


decimal_to_binary(10)

print("".join(binary[::-1]))
