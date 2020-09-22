'''
Ways to import modules:
1. import my_module
Now we would call the funtions as: my_module.function1()

2. import my_module as mod
Now we will call the function this way: mod.function1

3. from my_module import function1
Now we call the function just by its name.
But we cannot call other functions or variables this way.

4. from my_module import function1 as f1
Now we call the function just by its nickname (i.e. f1)
But we cannot call other functions or variables this way.

5. from my_module import function1 as f1, function2 as f2
This way we can call multiple functions and we can call them by their nick names

6. from my_module import *
This means, from my_module import everything!
This is the worst way!!
---------------------------------------------------------------------------------
# Now in order to see where python searches for modules we have to do this:
import sys
print(sys.path)
---------------------------------------------------------------------------------
As we can see it is only a list: Now we can append our own folder into that list
in oder to add our own modules by the following way:
import sys
sys.path.append('C:\\Users\\Yasir\\Documents\\mystuff\\python\\modules')
math random sys os datetime calendar functools
----------------------------------------------------------------------------------
In pycache folder, Python stores the compiled version of previously imported modules
to speed up the loading time of these modules.
'''
