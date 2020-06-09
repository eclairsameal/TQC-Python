import math
n = eval(input())
sum = 0
for i in range(2, n+1):
    sum+=1/(math.sqrt(i-1) + math.sqrt(i))
print("{:.4f}".format(sum))