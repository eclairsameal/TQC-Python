from math import pi, tan, pow
s = eval(input())
area = (5 * pow(s, 2))/(4 * tan(pi/5))
print('Area = {:.4f}'.format(area))