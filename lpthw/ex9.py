# INPUT FUNCTION
print("How old are you?")
age = input("Enter your age: ")
# Here age is saved as a string even if we enter an integer, the return
#type of input() is a STRING ONLY
print("How tall are you?")
height = input("Enter your height here: ")
print("How much do you weigh?")
weight = input("Enter your weight here: ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#Why can’t I do print("How old are you?" , input())? You can,
#but then the result of calling input() is never saved to a
#variable, and it’ll work in a strange way.
