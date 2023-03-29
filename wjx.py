import re
from meili_search import search

known_string = '只有（）的人在一起做事才会产生共鸣'

target_string = search(known_string)

# 将已知字符串中的（ ）替换成正则表达式中的特殊字符
known_string = known_string.replace("（）", "(.*)")

# 使用正则表达式匹配括号内的内容
pattern = re.compile(".*" + known_string + ".*")
match = pattern.match(target_string)

if match:
    result = match.group(1)
    print(result)
else:
    print("No match")
