import re
regex_object = re.compile(r'\d{3}-\d{3}-\d{4}')
match_object = regex_object.findall('Cell: 415-555-6666, Work: 416-555-7777')
# Returns a list
print(match_object[0])
print(match_object[1])
