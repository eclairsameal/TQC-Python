def input_num(n):
    n_l = []
    for i in range(n):
        n_l.append(int(input()))
    return n_l

n = 10
num_list = sorted(input_num(n))
sum = 0
for i in range(1, n-1):
    sum+=num_list[i]
print("{}".format(sum))
print("{:.2f}".format(sum/(n-2)))