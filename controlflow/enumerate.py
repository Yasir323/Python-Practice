# python code to demonstrate working of enumerate()

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)

string = 'We can do this with a list too'
ls = string.split(' ')
for key, val in enumerate(ls):
    print(key, val)
