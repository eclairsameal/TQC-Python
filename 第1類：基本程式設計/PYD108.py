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