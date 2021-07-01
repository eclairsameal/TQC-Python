f = open("read.txt")
string = f.read()
s = 0
sp_str = string.split()
for i in sp_str:
    s+=int(i)
print(s)
f.close()
