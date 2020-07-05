# Python code to demonstrate String encoding and decoding

# Initialising a string
a = 'GeeksforGeeks'

# Initialising a byte object
c = b'GeeksforGeeks'
print(type(a))
print(type(c))

# Encoding
d = a.encode('ASCII')
print(d)

print("Encoding successful") if d == c else print("Encoding unsuccessful")
# Decoding
e = c.decode('ASCII')
print(e)

print("Decoding successful") if e == a else print("Decoding unsuccessful")
