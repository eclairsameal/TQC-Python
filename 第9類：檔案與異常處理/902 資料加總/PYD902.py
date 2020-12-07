f = open("read.txt")
str = f.read()
sum = 0
sp_str = str.split()
for i in range(len(sp_str)):
    sum+=int(sp_str[i])
print(sum)
f.close()
