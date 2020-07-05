# FOR LOOP
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this kind of for loop goes throung a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# range(stop) -> range object
# range(start, stop[, step]) -> range object
# Return an object that produces a sequence of integers from start (inclusive)
# to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
# start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
# These are exactly the valid indices for a list of 4 elements.
# When step is given, it specifies the increment (or decrement).
 for i in range (0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
