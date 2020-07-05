from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")

print("Before we do that let's read it first.")
target = open(filename, 'r')
print(target.read())
target.close()

print("Are you sure you want to erase the contents of the file?")
print("Hit CTRL-C (^C) to cancel.")
print("Hit ENTER to erase.")

input("?")
target = open(filename, 'w')
print("Truncating the file, Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Let's write these three lines into the file.")

target.write(line1+"\n"+line2+"\n"+line3+"\n")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("Now, let's close this file.")
target.close()
