def input_num(n):
    n_l = []
    for i in range(n):
        n_l.append(eval(input()))
    return n_l

num_list = sorted(input_num(10))
list_len = len(num_list)
print("{} {} {}".format(num_list[list_len-1], num_list[list_len-2], num_list[list_len-3]))