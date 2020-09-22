# Case-insensitive matching
import re
'''
To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
'''
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
