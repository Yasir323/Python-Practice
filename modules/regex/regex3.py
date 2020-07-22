# Matching multiple groups with the pipeor '|'
import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Rey')
print(mo1.group())
#----------------------------------------------#
mo2 = heroRegex.search('Batman and Tina Fey')
print(mo2.group())
# First come first serve
#----------------------------------------------#
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
