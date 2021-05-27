import math
def print_point(x, y):
    print("( {} , {} )".format(x, y))  
x = eval(input())
y = eval(input())
x1 = eval(input())
y1 = eval(input())
print_point(x, y)
print_point(x1, y1)
print("Distance = {:.4f}".format(math.sqrt((math.pow(x-x1, 2) + math.pow(y-y1, 2)))))


import math
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print("({},{})".format(x1, y1))
print("({},{})".format(x2, y2))
distance = math.sqrt((math.pow(x1-x2, 2) + math.pow(y1-y2, 2)))
print("Distance = {:.4f}".format(distance))
