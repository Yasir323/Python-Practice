import os
print(os.name)

print(os.getcwd())
# Gives the current working directory

print(os.path.abspath('.'))
# To print the absolute path on your system

print(os.listdir('.'))
# To print files and directories in the current directory
#----------------------------------------------------------

'''
os.error:
All functions in this module raise OSError in the case of
invalid or inaccessible file names and paths, or other
arguments that have the correct type, but are not accepted
by the operating system. os.error is an alias for built-in
OSError exception.
'''
try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'GFG.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()

# Control jumps directly to here if
#any of the above lines throws IOError.
except IOError:

    # print(os.error) will <class 'OSError'>
    print('Problem reading: ' + filename)

# In any case, the code then continues with
# the line after the try/except
#---------------------------------------------------------------
print(os.environ)
print(os.getenv('Home'))
