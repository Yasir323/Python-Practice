# NAMESPACE AND SCOPE

# Python program processing global variable
count = 5


def some_method():
    global count
    count = count + 1
    print(count)


some_method()

# If we pass immutable objects like whole numbers,
# tuple or strings they are passed by value.

# Python code to demonstrate
# call by value
string = "Geeks"


def test(string):
    string = "GeeksforGeeks"
    print("Inside Function:", string)


# Driver's code
test(string)
print("Outside Function:", string)

# Whereas if we pass a mutable object to a function
# like a list, they are passed by reference


# Python code to demonstrate
# call by reference


def add_more(list):
    list.append(50)
    print("Inside Function", list)


# Driver's code
mylist = [10, 20, 30, 40]
add_more(mylist)
print("Outside Function:", mylist)
