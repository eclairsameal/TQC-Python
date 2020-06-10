a = int(input())
b = int(input())

def compute(a, b):
    sum = 0
    for i in range(a, b+1):
        sum+=i
    return sum

print(compute(a, b))