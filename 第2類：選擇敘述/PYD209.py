import math
x = eval(input())
y = eval(input())

dis = math.sqrt(pow(x-5, 2) + pow(y-6, 2))
if dis <= 15:
    print('Inside')
else:
    print('Outside')
"""
(x, y)-(5, 6)dis <= 15, output:Inside
(x, y)-(5, 6)dis >= 15, output:Outside
"""

