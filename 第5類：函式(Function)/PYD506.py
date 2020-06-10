import math
a = int(input())
b = int(input())
c = int(input())

def compute(a, b, c):
    de = b*b-4*a*c
    if de < 0:
        print("Your equation has no root.")
    elif de > 0:
        x = ((-b + math.sqrt(de))/(2*a))
        y = ((-b - math.sqrt(de))/(2*a))
        print("{}, {}".format(x, y))
    else:
        x = (-b)/(2*a)
        print("{}".format(x))
compute(a, b, c)
"""
Your equation has no root.
"""