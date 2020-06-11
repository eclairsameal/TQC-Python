num_list = []
total = 0
for i in range(12):
    num_list.append(eval(input()))
    if i%2==0:
        total+=num_list[i]
for j in range(12):
    print("{:>3d}".format(num_list[j]),end="")
    if j%3==2:print("")
print(total)
