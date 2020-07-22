# The wildcard character
'''
The . (or dot) character in a regular expression is called a wildcard and will
match any character except for a newline.
But it will return only string, not white spaces unless asked to do so.

Dot character will match just one character, which
is why the match for the text 'flat' in the following example matched only lat.
'''
import re
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
# Use the dot-star (.*) to stand in for that “anything.
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
'''
The dot-star uses greedy mode: It will always try to match as much text as
possible. To match any and all text in a nongreedy fashion, use the dot, star,
and question mark (.*?).
'''
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
