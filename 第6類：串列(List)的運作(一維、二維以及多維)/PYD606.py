rows = int(input())
cols = int(input())

li = [[i-j for i in range(0, cols)] for j in range(rows)]

for i in li:
    for j in i:
        print("{:>4d}".format(j), end="")
    print()
    
    
li =[]
for j in range(rows):
    l = []
    for i in range(0, cols):
        l.append(i-j)
    li.append(l)

for j in range(rows):
    for i in range(0, cols):
        print("{:>4d}".format(li[j][i]), end="")
    print()
