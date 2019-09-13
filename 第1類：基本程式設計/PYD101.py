#TODO
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

右詰め
print("|{:5} {:5}|".format(a, b))
print("|{:5} {:5}|".format(c, d))

#左詰め
print("|{:<5} {:<5}|".format(a, b))
print("|{:<5} {:<5}|".format(c, d))
'''
a = []
for i in range(4):
    x = int(input())
    a.append(x)
#右詰め
print("|{:5} {:5}|".format(a[0], a[1]))
print("|{:5} {:5}|".format(a[2], a[3]))

#左詰め
print("|{:<5} {:<5}|".format(a[0], a[1]))
print("|{:<5} {:<5}|".format(a[2], a[3]))