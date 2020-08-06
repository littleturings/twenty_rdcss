"""
re模块的基本操作
"""
import re
pattern = 'hello'
s = 'helloWorld hello'
# v = re.match(pattern,s)
v = re.search(pattern,s)
print(v)
# print(type(v))
# print(dir(v))
print(v.group())
print(v.span())