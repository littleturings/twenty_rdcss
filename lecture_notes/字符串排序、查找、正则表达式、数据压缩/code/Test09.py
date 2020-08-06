"""
v = re.match(r'(.+?)(\d+-\d+-\d+)','This is my tel:133-1234-1234')
print(v.group(1))
print(v.group(2))
"""
import re
#贪婪模式
# pattern = r'(.+)(\d+)-(\d+)-(\d+)'
# #非贪婪模式
# pattern = r'(.+?)(\d+)-(\d+)-(\d+?)'
# s = 'This is my tel:133-1234-1234'
# v = re.match(pattern,s)
# print(v)
# print(v.group(1))
# print(v.group(2))
# print(v.group(4))

#贪婪模式
# v= re.match(r'abc(\d+)','abc123')
# print(v.group(1))
#非贪婪模式
# v= re.match(r'abc(\d+?)','abc123')
# print(v.group(1))