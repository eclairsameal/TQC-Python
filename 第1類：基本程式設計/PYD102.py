a = []
for i in range(4):
    x = float(input())
    a.append(x)
    
#右詰め
print("|{:7.2f} {:7.2f}|".format(a[0], a[1]))
print("|{:7.2f} {:7.2f}|".format(a[2], a[3]))

#左詰め
print("|{:<7.2f} {:<7.2f}|".format(a[0], a[1]))
print("|{:<7.2f} {:<7.2f}|".format(a[2], a[3]))