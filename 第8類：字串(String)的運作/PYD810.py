def function():
    str_list = input().split(' ')
    num_list = [eval(str_list[i]) for i in range(len(str_list))]
    return max(num_list) - min(num_list)

n = int(input())
for i in range(n):
    print("{:.2f}".format(function()))