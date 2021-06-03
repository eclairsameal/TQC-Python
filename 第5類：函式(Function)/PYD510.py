num = int(input())

def Fibonacci(num):
    if(num==0 or num==1):
        return num
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)    
for i in range(num):
    print(Fibonacci(i), end=" ")
    

def fib_iterative(n):
    if n == 0:
        return 0
    f1, f2 = 1, 1
    for i in range(2, n):  # 當 n < 3 時不會進入迴圈
        f1, f2 = f2, f1 + f2
    return f2
for i in range(num):
    print(fib_iterative(i), end=" ")
