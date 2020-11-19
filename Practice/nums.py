def DisplayMenu():
    header = "*" * 9 + " " + "MENU" " " + "*" * 8
    print(header)
    print("1.  Display the list")
    print("2.  Search for a number in the list")
    print("3.  Find the max value in the list")
    print("4.  Replace a number in a specified position")
    print("5.  Count occurrences of a number")
    print("6.  Quit")
    selection = int(input("Enter a selection: "))
    print()
    return selection


def DisplayList(theList):
    print("The contents of the list:")
    print(theList)
    print()


def FindMax(theList):
    a = theList[0]
    for element in theList:
        if a < element:
            a = element
    return a


def ReplaceValue(theList, position, newValue):
    theList[position] = newValue


def CountValue(theList, value):
    counter = 0
    for element in theList:
        if element == value:
            counter += 1
    return counter


def Main():
    file = open("numbers.py")
    number = int(file.readline().strip())
    ls = []
    while(number != -99999):
        ls.append(number)
        number = int(file.readline().strip())

    choice = DisplayMenu()
    while choice != 6:
        if choice == 1:
            DisplayList(ls)

        elif choice == 2:
            number_to_find = int(input("Enter the number to search for: "))
            if number_to_find in ls:
                print(f"The number {number_to_find} is in the list")
            else:
                print(f"The number {number_to_find} is not in the list")
            print()

        elif choice == 3:
            max = FindMax(ls)
            print(f"The max value in the list is {max}")
            print()

        elif choice == 4:
            print(f"The length of the list is {len(ls)}")
            position = int(input("Enter the list position to replace: "))
            if position > len(ls):
                print("Invalid list position. No value replaced.")
            else:
                replacement = int(input("Enter the replacement value: "))
                ReplaceValue(ls, position, replacement)
            print()

        elif choice == 5:
            value = int(input("Enter the value to count: "))
            count = CountValue(ls, value)
            print(f"The number {value} occurs {count} times.")
            print()

        elif choice == 6:
            break

        else:
            print("Invalid selection. Try again.")
            print()

        choice = DisplayMenu()


Main()
