num = int(input())

def Fibonacci(num):
    if(num==0 or num==1):
        return num
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)
    
for i in range(num):
    print(Fibonacci(i), end=" ")