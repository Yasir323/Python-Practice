# MORE PRACTICE
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with the logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("--------------------------------")
print(poem)
print("--------------------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    # Here the function is returning a list of
    # variables (or simply a LIST)

start_point = 1000
beans, jars, crates = secret_formula(start_point)
# Here the three values returned by the function are
# stored is 3 variables IN ORDER

# REMEMBER ANOTHER WAY TO FORMAT A STRING
print("With a starting point of: {}".format(start_point))
#iT'S JUST LIKE WITH AN f"" STRING
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point / 10

print("We can also do it this way:")
formula = secret_formula(start_point)
# NOW THE THREE VALUES RETURNED BY THE FUNCTION WILL BE PLACED
# INSIDE A LIST. tHIS IS AN EASY WAY TO APPLY A LIST TO A
# FORMAT STRING
print("we'd have {} beans, {} jars and {} crates.".format(*formula))
