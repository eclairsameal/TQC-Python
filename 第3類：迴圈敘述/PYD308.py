n=eval(input())
for i in range(1,n+1):
    s=eval(input())
    a=0
    s1=s
    while s!=0:
        num=s%10
        a=a+num
        s=s//10
    print("Sum of all digits of {:d} is {:d}".format(s1,a))