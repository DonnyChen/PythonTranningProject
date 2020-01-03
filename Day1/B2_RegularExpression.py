import re

pattern = "([0-9]*)([a-z]*)([0-9]*)"
'''
* 匹配前面的子表达式任意次 {0，n}

'''
txt = '123abc456'

result = re.match(pattern, txt).group(0)
print(result)
result1 = re.match(pattern, txt).group(1)
result2 = re.match(pattern, txt).group(2)
result3 = re.match(pattern, txt).group(3)

resultGroups = re.match(pattern, txt).groups()

print(result1)
print(result2)
print(result3)
print(resultGroups)
