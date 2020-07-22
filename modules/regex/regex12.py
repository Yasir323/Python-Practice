# Matching Newlines with the Dot Character
'''
By passing re.DOTALL as
the second argument to re.compile(), you can make the dot character match
all characters, including the newline character.
'''
import re
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \
\nUphold the law.').group())


newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent. \
\nUphold the law.').group())
