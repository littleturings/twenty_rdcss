"""
search:
查找
findall:
查找所有
sub:
替换
split:
拆分
"""
import re
# s = 'C语言阅读次数为:999次,C++阅读次数为：1000次，Python阅读次数为:10000次'
# pattern = r'\d+'
# # v = re.match(pattern,s)
# # v = re.search(pattern,s)
# # v = re.findall(pattern,s)
# # print(v)
#
# #sub的用法
# # str1 = re.sub(pattern,'100',s,count=0)
# # print(str1)
# #可以基于一个函数来进行处理
# def replace(result):
#     return  str(int(result.group())+1)
# str1 = re.sub(pattern,replace,s)
# print(str1)

# split的用法
s = 'He say:Hello,World'
pattern = r'\s|:|,'
list1 = re.split(pattern,s)
print(list1)


