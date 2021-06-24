def input_num(n):
    n_l = []
    for i in range(n):
        n_l.append(int(input()))
    return n_l

n = 10
num_list = input_num(n)
m_num = 0
for i in range(n):
    if num_list.count(num_list[i]) > num_list.count(num_list[m_num]):
        m_num = i   
print(num_list[m_num])
print(num_list.count(num_list[m_num]))


