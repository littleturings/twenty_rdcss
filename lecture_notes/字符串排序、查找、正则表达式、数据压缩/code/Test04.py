"""
*	匹配前一个字符出现0次或者无限次（可有可无）
+	匹配前一个字符出现1次或者无限次(至少有1次)
？	匹配前一个字符串出现1次或者0次(要么1次要么没有)
{m}	匹配前一个字符出现m次
{,m}	匹配前一个字符至少出现m次
{m,n}	匹配前一个字符出现m到n次
"""
import re
#'*'的使用
# pattern = '\d*'
# # s = '123abc'
# s = 'abc'
# v = re.match(pattern,s)
# print(v)

#'+'的使用
# pattern = '\d+'
# # s = '123abc'
# s = 'abc'
# v = re.match(pattern,s)
# print(v)

#'?'的使用  表示可有(只出现一次)可无(0次)
# pattern = '\d?'
# # s = '123abc'
# s = 'abc'
# v = re.match(pattern,s)
# print(v)

#'{m}'的使用，匹配前一个字符出现m次
# pattern = '\d{2}'
# # pattern = '\d{2,4}'
# # pattern = '\d{3,}'
# s = '12345678abc'
# v = re.match(pattern,s)
# print(v)

#匹配出一个字符串首字母为大写字符，后边都是小写字符，这些小写字母可有可无
# pattern = '[A-Z][a-z]*'
# s = 'Hello'
# s = 'HEllo'
# v = re.match(pattern,s)
# print(v)
#匹配出有效的变量名 变量名: 大写字母，小写字母，数字，下滑线
# pattern = '[A-Za-z_][A-Za-z0-9_]*'
# pattern = '[A-Za-z_]\w*'
# s = 'Ab2_'
# s = '2c'
# s = '_2c'
# v = re.match(pattern,s)
# print(v)

#匹配出1-99之间的数字
# pattern = '[1-9][0-9]?'
# # s = '0'
# s = '10'
# s = '99'
# v = re.match(pattern,s)
# print(v)

#匹配出一个随机密码8-20位以内 {8,20}  大写字母小写字母，数字，下滑线
# pattern = '\w{8,20}'
# s = 'abc123_123'
# v = re.match(pattern,s)
# print(v)




