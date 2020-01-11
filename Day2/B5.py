import decimal
import random
import math


'''set
去除重复，不关心序列
'''

x = set("pytonn") 
x = set(['1',1])
print(x)

#x1 = set([[1,2,3], [4,5, 6]])
#print(x)

d1 = 3.141592653589790007373494518
d1 = d1 +2
print(d1)

d2 = decimal.Decimal(3.141592653589790007373494518)
d2 += 2
print(d2)

int_a = 200
int_a += 6.666666

print(type(int_a))
print(int_a)
print(int(int_a))

float_a = 1
print(float(float_a))

num_a = 10 / 4 #真除法
num_b = 10 // 4 # Floor除法
num_c = "%.3f" % num_a
print(num_a, num_b, num_c)

complex_a = complex(2, 3)
print(complex_a)
complex_a *= 2
print(complex_a)
print(complex_a.real)
print(complex_a.imag)
print(complex_a.conjugate())

#complex_b = (2+3j)


