'''
Since there is no main() function in Python, when the command to run
a python program is given to the interpreter, the code that is at
level 0 indentation is to be executed. However, before doing that,
it will define a few special variables. __name__ is one such special
variable. If the source file is executed as the main program, the
interpreter sets the __name__ variable to have a value “__main__”.
If this file is being imported from another module, __name__ will
be set to the module’s name.
__name__ is a built-in variable which evaluates to the name of the
current module. Thus it can be used to check whether the current
script is being run on its own or being imported somewhere else
by combining it with if statement.
'''

print("File __name__ = %s" %__name__)

if __name__ == "__main__":
    print("File is being run directly")
else:
    print("File is being imported")
