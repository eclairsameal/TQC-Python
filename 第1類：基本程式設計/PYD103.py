a = []
for i in range(4):
    x = str(input())
    a.append(x)
#右詰め
print("|{:>10s} {:>10s}|".format(a[0], a[1]))
print("|{:>10s} {:>10s}|".format(a[2], a[3]))

#左詰め
print("|{:<10s} {:<10s}|".format(a[0], a[1]))
print("|{:<10s} {:<10s}|".format(a[2], a[3]))