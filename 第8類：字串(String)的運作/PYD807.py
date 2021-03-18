str_list = input().split(' ')

for i in range(len(str_list)):     # string -> int
    str_list[i] = int(str_list[i])

#str_list = [int(str_list[i]) for i in range(len(str_list))] # string -> int

#str_list = list(map(int, str_list)) # string -> int

#print(str_list)
list_sum = sum(str_list)
print("Total = {:d}".format(list_sum))
print("Average = {:.1f}".format(list_sum/len(str_list)))
