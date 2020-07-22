# Substituting Strings with the sub() method
import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
'''
Say you want to censor the names of the secret agents by
showing just the first letters of their names. To do this, you could use the
regex Agent (\w)\w* and pass r'\1****' as the first argument to sub(). The \1
in that string will be replaced by whatever text was matched by group 1—
that is, the (\w) group of the regular expression.
'''
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent \
Eve knew Agent Bob was a double agent.'))
