f_name = input()
n = int(input())

with open("read.txt","r",encoding="UTF-8") as fp:
    data = sorted(fp.read().split())
setdata = sorted(set(data))
for i in setdata:
    if data.count(i) == n:
        print(i)
