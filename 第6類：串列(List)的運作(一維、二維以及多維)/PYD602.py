strlist = ['J', 'Q', 'K', 'A']
intlist = [11, 12, 13, 1]

sum = 0

for i in range(5):
    x = input()
    if(x.isdigit()):
        sum += int(x)
    else:
        sum += intlist[strlist.index(x)]
print(sum)