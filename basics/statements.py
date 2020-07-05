# MULTI-LINE STATEMENTS
"""Statements in Python can be extended to one
or more lines using parentheses (),
braces {}, square brackets [], semi-colon (;),
continuation character slash (\)"""

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

b = (1 * 2 * 3 *
     4 * 5)

footballer = ['Messi',
              'Cristiano',
              'Neymar']

c = {1 + 2 + 3 + 4 +
     5 + 6 + 7 + 8 + 9}; d = a + b
print(a)
print(b)
print(c)
print(d)
print(footballer)


"""Some statements may become very long and may
force you to scroll the screen left and right
frequently. You can fit your code in such a
way that you do not have to scroll here and there.
Python allows you to write a single statement in
multiple lines, also known as line continuation.
Line continuation enhances readability as well."""

no_of_teachers = 10
no_of_male_students = 20
no_of_female_students = 30
if (no_of_teachers == 10 and no_of_female_students == 30
    and no_of_male_students == 20):
    print("ok")
