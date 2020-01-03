'''
print("Hello Donny!")
print("Hello Paddy", end='\n')
print("hello Lilith", end="")
print("Hello Paddy", end='\n')
'''

mystr = "abcdefg"
"""
print(mystr[-3])
print(mystr[len(mystr)-3])


When constructing a slice, as in [6:11], the first index number is where the slice starts (inclusive), and the second index number is where the slice ends (exclusive), which is why in our example above the range has to be the index number that would occur just after the string ends.

print(mystr[:-1])
print(mystr[-1])
print(mystr[::-1])
print(mystr[5])
print(mystr[5:1:-1])
"""
print(mystr.find('e'))
print(mystr.replace('e', 'donny'))
print(mystr.join('join'))
print("8".join(mystr))
print(mystr.upper())
print(mystr.isalpha())
print(mystr.endswith('g'))
print(mystr.isdigit())

token = "11,22,33,44,55,66"
tokenlist = token.split(',')
print(type(token))
print(type(tokenlist))
print(token)
print(len(token))
print(len(tokenlist))

print(ord('\n'))
print(ord('\r'))
print(ord('a'))