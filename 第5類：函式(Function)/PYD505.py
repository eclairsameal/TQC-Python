a = input()
x = int(input())
y = int(input())

def compute(a, x, y):
    for i in range(1, x*y+1):
        print(a, end=" ")
        if(i%x==0):
            print()
compute(a, x, y)