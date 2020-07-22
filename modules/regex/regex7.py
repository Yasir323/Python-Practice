# Matching Specific Repetitions with Curly Brackets
import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
#----------------------------------------------------#
mo2 = haRegex.search('Ha')
print(mo2 == None)
# Python's Regular expressions are greedy by default, i.e.
# in ambiguous situation they'll match the longest string possible
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
# Non greedy version has a closing curly bracket followed by a '?'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
