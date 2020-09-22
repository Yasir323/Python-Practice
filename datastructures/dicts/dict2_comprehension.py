# Dictionary comprehension
print("Let's look at a list comprehension first:")
squares_list = [x ** 2 for x in range(5)]
print(squares_list)

print("Now let's take a look at sets:")
sqaures_sets = {x ** 2 for x in range(5)}
print(sqaures_sets)

print("Dictionary comprehension:")
squares_dict = {x : x ** 2 for x in range(5)}
print(squares_dict)

print("What about tuples?")
print("If we do the same thing as above we get a generator object, not a 'Tuple dictionary:")
squares_tuple_does_not_exist = (x ** 2 for x in range(5))
print(squares_tuple_does_not_exist)
