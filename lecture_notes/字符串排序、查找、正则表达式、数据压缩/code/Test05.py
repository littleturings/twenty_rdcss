import re
# s = '\n123'
# s = r'\n123'
s = '\\\\n123'
print(s)
# pattern = '\\n\d{3,}'
# pattern = '\\\\\\\\n\d{3,}'
pattern = r'\\\\n\d{3,}'
v = re.match(pattern,s)
print(v)