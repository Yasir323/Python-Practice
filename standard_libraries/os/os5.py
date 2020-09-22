import os
'''
Calling os.path.getsize(path) will return the size in bytes of the file in
the path argument.

Calling os.listdir(path) will return a list of filename strings for each file
in the path argument.
'''
print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
print(os.listdir('C:\\Windows\\System32'))

'''
Calling os.path.exists(path) will return True if the file or folder referred
to in the argument exists and will return False if it does not exist.

Calling os.path.isfile(path) will return True if the path argument exists
and is a file and will return False otherwise.

Calling os.path.isdir(path) will return True if the path argument exists
and is a folder and will return False otherwise.
'''
print(os.path.exists('C:\\Windows'))
print(os.path.exists('C:\\some_made_up_folder'))
print(os.path.isdir('C:\\Windows\\System32'))
print(os.path.isfile('C:\\Windows\\System32'))
print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))
