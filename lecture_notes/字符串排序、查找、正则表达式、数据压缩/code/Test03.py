"""
.	匹配任意一个字符（除了\n）
[]	匹配列表中的字符
\d	匹配数字，即0-9
\D	匹配非数字
\s	匹配空白、即空格（\n,\t）
\S	匹配非空格
\w	匹配单词字符，即a-z,A-Z,0-9,_
\W	匹配非单词字符
"""
import re
#'.'的验证
# pattern = '.'
# s = 'a'
# s = 'A'
# s = '0'
# s = '_'
# s = '\n'
# v = re.match(pattern,s)
# print(v)

#'\d'与\D的验证
# pattern = '\d'
# pattern = '\D'
# s = '0'
# s = '9'
# s = 'a'
# s = '_'
# v = re.match(pattern,s)
# print(v)

#'\s与\S的验证'
# pattern = '\s'
# pattern = '\S'
# s = ' '
# s = '\t'
# s = '\n'
# s = 'a'
# v = re.match(pattern,s)
# print(v)

#'\w与\W的验证'
# pattern = '\w'
# pattern = '\W'
# s = 'a'
# s = 'A'
# s = '0'
# s = '_'
# s = '-'
# v = re.match(pattern,s)
# print(v)

#[]的验证
# pattern = '[13578]'
# s = '1'
# s = '3'
# s = '5'
# s = '7'
# s = '8'
# v = re.match(pattern,s)
# print(v)
#匹配手机号的话 11位数
pattern = '1[35789]\d\d\d\d\d\d\d\d\d'
# s = '13812341234'
# s = '23812341234'
s = '15812341234'
v = re.match(pattern,s)
print(v)

