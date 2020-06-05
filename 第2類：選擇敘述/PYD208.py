num = eval(input())

# solution 1
print('{0:X}'.format(num))

# solution 2
hex = ['A', 'B', 'C', 'D', 'E', 'F']
if num <= 9:
    print(num)
else:
    print(hex[num-10])