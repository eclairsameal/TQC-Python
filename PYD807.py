str_list = input().split(' ')
num_list = [int(str_list[i]) for i in range(len(str_list))]

list_sum = sum(num_list)
print("Total = {:d}".format(list_sum))
print("Average = {:.1f}".format(list_sum/len(num_list)))

"""
Total = _
Average = _ 
"""