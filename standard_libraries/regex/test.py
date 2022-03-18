import re

name = 'durg'
# pattern = re.compile(name+'[^a-z]+|'+name+r'(\s\w+)+')
pattern = re.compile(r'\b'+name+r'\b')
print(pattern.search('durg').group() if pattern.search('durg') is not None else 'Not Found')
print(pattern.search('durgapur').group() if pattern.search('durgapur') is not None else 'Not Found')
print(pattern.search('durg bypass').group() if pattern.search('durg bypass') is not None else 'Not Found')
