# The caret and dollar Sign characters
'''
You can also use the caret symbol (^) at the start of a regex to indicate that
a match must occur at the beginning of the searched text.

You can put a dollar sign ($) at the end of the regex to indicate the string must end
with this regex pattern.

 ^ and $ together to indicate that the entire string must match the regex
'''
import re
beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
print(mo1.group())
print(beginsWithHello.search('He said hello.') == None)

endsWithNumber = re.compile(r'\d$')
mo2 = endsWithNumber.search('Your number is 42')
print(mo2.group())
print(endsWithNumber.search('Your number is forty two.') == None)

wholeStringIsNum = re.compile(r'^\d+$')
mo3 = wholeStringIsNum.search('1234567890')
print(mo3.group())
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)
