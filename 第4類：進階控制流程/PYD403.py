a = int(input())
b = int(input())
sum = 0
len = 0
for i in range(a, b+1):
    if(i%4==0 or i%9==0):
        print("{:<4d}".format(i), end="")
        len+=1
        sum+=i
        if(len%10==0):
            print("")
print("\n{}\n{}".format(len, sum))
