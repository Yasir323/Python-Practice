types_of_people = 10
# variable is expressed in the form of a "print" string
x = "There are %d types of people." % 10

binary = "binary"
do_not = "don't"
#Same as x but here a different format is used, a string is
#put inside a string twice(1),(2)
y = f"Those who know {binary} and those who {do_not}."

# now we do not need to type everything in the print parameters,
#Just print the variables x & y
print(x)
print(y)
#(3)
print("I said: '%s'." %x)

#What is the difference between %r and %s?
#We use %r for debugging, since it displays the “raw” data of the
# variable, but we use %s and others for displaying to users.

#What’s the point of %s and %d when you can just use %r?
#The %r is best for debugging, and the other formats are for
#actually displaying variables to users.

#By default %r represents strings in single quotes, but if there
#is a single quote used inside of the string it will represent
#string in double quotes.
#(4)
print("I also said: %r." %y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#THis line is just filling the curly braces of above varible
# with hilarious
print(joke_evaluation.format(hilarious))

w = "This is the left side of... "
e = "a string with a right side."
#concatenation of 2 strings
print (w+e)

#I tried putting Chinese (or some other non- ASCII characters)
#into these strings, but %r prints out weird symbols.
#Use %s to print that instead and it’ll work
