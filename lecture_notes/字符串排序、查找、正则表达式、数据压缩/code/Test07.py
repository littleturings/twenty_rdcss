"""
丨	匹配左右任意一个表达式
(ab)	将括号中的字符作为一个分组
\num	引用分组num匹配到的字符串
(?p<name>)	分别起组名
(?p=name)	引用别名为name分组匹配到的字符串

匹配0-100之间所有的数字

0-99   |  100

"""
import re
# pattern = r'[1-9]?\d$|100$'
# s = '0'
# s = '10'
# # s = '9000'
# s = '100'
# # s = '1000'
# v = re.match(pattern,s)
# print(v)

#匹配座机号码  区号 - 电话号 {5,8}  ()
# pattern = r'(\d{3,4})-([1-9]\d{4,7})$'
# # pattern = r'\d{3,4}-[1-9]\d{4,7}$'
# s = '010-56668888'
# v = re.match(pattern,s)
# print(v)
# print(v.group())
# print(v.group(1))
# print(v.group(2))
# print(v.groups())
# print(v.groups()[0])
# print(v.groups()[1])

#匹配出网页标签内的数据  <html><title></title></html>
# pattern = r'<.+><.+>.+</.+></.+>'
# pattern = r'<(.+)><(.+)>.+</\2></\1>'
# s = "<html><h1>我是标题</header></body>"
# v = re.match(pattern,s)
# print(v)

#匹配分组别名以及引用别名
# s = '<html><h1>我是一号字体</h1></html>'
# # pattern = r'<(.+)><(.+)>.+</\2></\1>'
# pattern = r'<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>'
# v = re.match(pattern,s)
# print(v)


