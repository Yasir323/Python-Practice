# Defining functions within a function

def hi(name="Yasir"):
    print("Inside hi.")
    # Defining functions within a function
    def greet():
        return "Inisde greet."
    def welcome():
        return "Inside welcome."

    print(greet())
    print(welcome())
    print("Inside hi again.")

hi()
# print(greet())
# NameError: name 'greet' is not defined
