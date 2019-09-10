# TODO
list = []
while True :
    x = input()
    if(x == 'end'):
        break
    list.append(x)
tup = tuple(list)
print(tup)
pr_tup = list[:3]
print(tuple(pr_tup))
pr_tup = list[-3:]
print(tuple(pr_tup))