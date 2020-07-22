# making your own character classes
import re
'''
You can define
your own character class using square brackets.
For example, the character class [aeiouAEIOU] will
match any vowel, both lowercase and uppercase.
'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
'''
You can also include ranges of letters or numbers by using a hyphen.
For example, the character class [a-zA-Z0-9] will match all lowercase letters,
uppercase letters, and numbers.
By placing a caret character (^) just after the character class’s opening
bracket, you can make a negative character class. A negative character class
will match all the characters that are not in the character class.
'''
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))
