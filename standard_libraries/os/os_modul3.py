# Python program to explain os.close() method

# importing os module
import os

# Path
fd = "GFG.txt"


# open the file and get
# the file descriptor associated
# with it using os.open() method
file = os.open(fd, os.O_WRONLY)


# Perform some operation
# Lets write a string
s = "GeeksForGeeks: A computer science portal for geeks"

# Convert string to bytes object
line = str.encode(s)

# Write string to file referred by
# by the file descriptor
os.write(file, line)


# close the file descriptor
os.close(file)
print("File descriptor closed successfully")
