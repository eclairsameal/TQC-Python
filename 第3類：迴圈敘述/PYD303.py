n = eval(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("{:>4}".format(i*j), end="")
    print()