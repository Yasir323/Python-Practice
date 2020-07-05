from sys import argv
script, source = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(source)

print("First let's print the whole file:")
print_all(current_file)

#In Python, there is no rewind function
#so we defined one by using seek(0) 
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
