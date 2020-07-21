rows = int(input())
cols = int(input())

li = [[i-j for i in range(0, cols)] for j in range(rows)]

for i in li:
    for j in i:
        print("{:>4d}".format(j), end="")
    print()
    