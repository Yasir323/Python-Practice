# CONDITIONS, LOOPS, FUNCTIONS
def calculator(operation, x, y):
    if operation == 1:
        print(x + y)
    elif operation == 2:
        print(x - y)
    elif operation == 3:
        print(x*y)
    elif operation == 4:
        print(x**y)
    else:
        print(x/y)


x = int(input("Enter first number."))
y = int(input("Enter first number."))
while True:
    print("Press 0 to escape.")
    print("Press 1 to add.")
    print("Press 2 to subtract.")
    print("Press 3 to multiply.")
    print("Press 4 to power.")
    print("Press 5 to divide.")
    operation = int(input("What do u want to do?"))
    if operation in range(1, 6):
        calculator(operation, x, y)
    elif operation == 0:
        exit()
    else:
        continue
