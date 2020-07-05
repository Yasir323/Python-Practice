from sys import argv
script, filename = argv

#Open the file
txt = open(filename)

#printing the file
print(f"Here's you file {filename}:")
#We call a function on txt named read. What you get
#back from open is a file, and it also has commands
#you can give it. You give a file a command by using
#the . (dot or period), the name of the command, and
#parameters, just like with open and input. The
#difference is that txt.read() says, ”Hey txt! Do your
#read command with no parameters!”
print(txt.read())

txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
