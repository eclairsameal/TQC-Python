num = eval(input())

# solution 1
print('{0:X}'.format(num))

# solution 2
hex = ['A', 'B', 'C', 'D', 'E', 'F']
if num <= 9:
    print(num)
else:
    print(hex[num-10])
    
# solution 3
num = int(input())
if num <= 9:
    print(num)
elif num == 10:
    print('A')
elif num == 11:
    print('B')
elif num == 12:
    print('C')
elif num == 13:
    print('D')
elif num == 14:
    print('E')
elif num == 15:
    print('F')
