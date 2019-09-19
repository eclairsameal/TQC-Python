num = []
for i in range(5):
    x = eval(input())
    num.append(x)
print(num[0], num[1], num[2], num[3], num[4])
print("Sum = {:.1f}".format(sum(num)))
print("Average = {:.1f}".format(sum(num)/len(num)))