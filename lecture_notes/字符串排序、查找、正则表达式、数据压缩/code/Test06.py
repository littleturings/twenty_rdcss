"""
使用示例1 匹配QQ邮箱    5-10   @qq.com
"""
import re
# 匹配结尾
# pattern = r'[1-9]\d{4,9}@qq.com'
# pattern = r'[1-9]\d{4,9}@qq.com$'
# s = '12345@qq.com'
# # s = '12345@qq.com.@126.com'
# v = re.match(pattern,s)
# print(v)

# 匹配单词边界\b
# pattern = r'.*\ber'
# pattern = r'.*er\b'
# # s = '123,eroa'
# s = '123,oaer'
# v = re.match(pattern,s)
# print(v)

# 匹配单词边界\B
# pattern = r'.*\Ber'
pattern = r'.*er\B'
# s = '123,eroa'
s = '123,oaer'
v = re.match(pattern,s)
print(v)

