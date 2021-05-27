from math import pi, tan, pow
n = eval(input())
s = eval(input())
area = (n * pow(s, 2))/(4 * tan(pi/n))
print('Area = {:.4f}'.format(area))


import math
n = eval(input())
s = eval(input())
area = (n * math.pow(s, 2))/(4 * math.tan(math.pi/n))
print('Area = {:.4f}'.format(area))
