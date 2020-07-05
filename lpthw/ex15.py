#FUNCTIONS
#this one is like your scripts with argv
# args, here, is a LIST containing two variables arg1 and arg2
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#That *args was pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
#What does the * in *args do?
#That tells Python to take all the arguments to the
#function and then put them in args as a list. It’s
#like argv that you’ve been using but for functions.
#It’s not normally used too often unless specifically needed

#This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Yasir", "Jafri")
print_two_again("Yasir", "Jafri")
print_one("First!")
print_none()
