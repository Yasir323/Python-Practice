"""
In String module, Template Class allows us
to create simplified syntax for output
specification. The format uses placeholder
names formed by $ with valid Python identifiers
(alphanumeric characters and underscores).
Surrounding the placeholder with braces
allows it to be followed by more alphanumeric
letters with no intervening spaces. Writing $$ creates a single escaped $:
"""
# A Simple Python templaye example
from string import Template

# Create a template that has placeholder for value of x
t = Template('x is $x')

# Substitute value of x in above template
print(t.substitute({'x': 1}))

# List Student stores the name and marks
# of three students
Student = [('Ram', 90), ('Ankit', 78), ('Bob', 92)]

# We are creating a basic structure to
# print the name and

# marks of the students.
t = Template('Hi $name, you have got $marks marks')

for i in Student:
    print(t.substitute(name=i[0], marks=i[1]))
