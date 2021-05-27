n1 = eval(input())
n2 = eval(input())
n3 = eval(input())
n4 = eval(input())
n5 = eval(input())
print(n1, n2, n3, n4, n5)
n_sum = n1 + n2 + n3 + n4 +n5
print("Sum = {:.1f}".format(n_sum))
print("Average = {:.1f}".format(n_sum/5))

num = []
for i in range(5):
    x = eval(input())
    num.append(x)
print(num[0], num[1], num[2], num[3], num[4])
print("Sum = {:.1f}".format(sum(num)))
print("Average = {:.1f}".format(sum(num)/len(num)))
