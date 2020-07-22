import os
# Get the current working directory
print(os.getcwd())

# Change the current working directory
print(os.chdir('C:\\Users\\Yasir\\mystuff\\python\\modules'))
print(os.getcwd())
print(os.chdir('C:\\Users\\Yasir\\mystuff\\python\\modules\\os'))
print(os.getcwd())

'''
Since in Windows paths are written using backslash but OS X Linus use forward slash.
 If you want your programs to work on all operating
systems, you will have to write your Python scripts to handle both cases.
Fortunately, this is simple to do with the os.path.join() function. If you
pass it the string values of individual file and folder names in your path,
os.path.join() will return a string with a file path using the correct path
separators.
'''
print(os.path.join('usr', 'bin', 'spam'))

# Creating new directories
# os.makedirs(os.path.join('C', 'delicious', 'walnut', 'waffles'))
'''
This will create not just the C:\delicious folder but also a walnut folder
inside C:\delicious and a waffles folder inside C:\delicious\walnut.
'''


# Handling absolute and relative paths.
'''
Calling os.path.abspath(path) will return a string of the absolute path
of the argument. This is an easy way to convert a relative path into an
absolute one.
'''
print(os.path.abspath('.')) # Dot means current folder, hence it'll return cwd.
'''
 Calling os.path.isabs(path) will return True if the argument is an
 absolute path and False if it is a relative path.
'''
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
'''
Calling os.path.relpath(path, start) will return a string of a relative path
from the start path to path. If start is not provided, the current working
directory is used as the start path.
'''
print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\Users\\Yasir'))

'''
Calling os.path.dirname(path) will return a string of everything that comes
before the last slash in the path argument. Calling os.path.basename(path) will
return a string of everything that comes after the last slash in the path argument.
'''
path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))
'''
If you need a path’s dir name and base name together, you can just call
os.path.split() to get a tuple value with these two strings.
'''
print(os.path.split(path))
print(path.split(os.path.sep))
