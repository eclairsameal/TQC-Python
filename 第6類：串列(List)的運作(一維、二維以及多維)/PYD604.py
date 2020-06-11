def input_num(n):
    n_l = []
    for i in range(n):
        n_l.append(int(input()))
    return n_l

n = 10
num_list = input_num(n)
for i in range(n):
    if num_list.count(num_list[i]) > 1:
        print(num_list[i])
        print(num_list.count(num_list[i]))
        break