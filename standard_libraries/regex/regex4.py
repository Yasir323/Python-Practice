# Optional matching with question mark
import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman.')
print(mo1.group())
#--------------------------------------------------#
mo2 = batRegex.search('The adventures of Batwoman.')
print(mo2.group())
#--------------------------------------------------#
mo3 = batRegex.search('The adventures of Batwoman and Batman.')
print(mo3.group())
