from collections import Counter
c = Counter(['Python', 'JS'])
print(type(c))
print(c)
c.update(['Python', 'C++'])
print(c)
c.update(['Python', 'JS', 'C++'])
print(c)
