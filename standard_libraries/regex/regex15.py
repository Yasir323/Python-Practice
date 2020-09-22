# Managing complex regexes
'''
telling the re.compile() function
to ignore whitespace and comments inside the regular expression string.
This “verbose mode” can be enabled by passing the variable re.VERBOSE as
the second argument to re.compile().
'''
import re
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)
#---------------------------------------------------------------------------------
# Combining re.ignorecASe, re.dotAll, and re.VerBoSe

# re.compile() function takes only a single value as its second argument.
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
