# Use of underscores
'''
SINGLE UNDERSCORE:

1. In Interpreter:
_ returns the value of last executed expression value in Python Prompt/Interpreter

2. Many times we do not want return values at that time assign those values to
Underscore. It used as throwaway variable.

3. Single Leading underscore in class:
So basically one underscore in the beginning of a method, function or data member
means you shouldn’t access this method because it’s not part of the API.
    Name prefixed by an underscore is treated as non-public. If we specify import *
all the methods/classes starting with _ will not be imported. Python does not specify
truly private so this ones can be call directly from other modules if it is specified
in __all__, We also call it weak Private.
    Main purpose for __ is to use variable/method in class only If you want to use it
outside of the class you can make public api

DOUBLE UNDERSCORE:

In name mangling process any identifier with two leading underscore and one trailing
underscore is textually replaced with _classname__identifier where classname is the
name of the current class. It means that any identifier of the form __geek (at
least two leading underscores or at most one trailing underscore) is replaced with
_classname__geek, where classname is the current class name with leading
underscore(s) stripped.

Name with start with __ and ends with same considers "magic methods" in Python.
Python provide this methods to use it as the operator overloading depending on the user.
Python provides this convention to differentiate between the user defined function
with the module’s function.
'''
