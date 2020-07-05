'''
UNZIP: Unzipping means converting the zipped values
back to the individual self as they were. This is
done with the help of “*” operator.
'''
name = ['Luffy', 'Sabo', 'Ace', 'Garp']
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip to map values
mapped = zip(name, roll_no, marks)

# converting values to print as a set
mapped = list(mapped)

print(mapped)

# Unzipping values
namez, roll_noz, marksz = zip(*mapped)

print(type(namez))  # The return type after unzipping is a tuple
print(namez)
print(roll_noz)
print(marksz)
