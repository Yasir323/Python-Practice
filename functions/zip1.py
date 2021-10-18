'''
The purpose of zip() is to map the similar index of multiple
containers so that they can be used just using as single entity.

Syntax : zip(*iterators)
Parameters : Python iterables or containers ( list, string etc )
Return Value : Returns a single iterator object, having mapped
values from all the containers.
'''
name = ['Luffy', 'Sabo', 'Ace', 'Garp']
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip to map values
mapped = zip(name, roll_no, marks)
print(type(mapped))
for name, roll, marks in mapped:
    print(name)
    print(roll)
    print(marks)
# converting values to print as a set
mapped = set(mapped)

print(mapped)
