n = eval(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:<2}* {:<2}= {:<4}".format(j, i, i*j), end='')
    print()