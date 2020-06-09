amount = eval(input())
rate = eval(input())
month = eval(input())
print('%s \t  %s' % ('Month', 'Amount'))
total = amount
for i in range(month):
    total+=total*rate/1200
    print('%3d \t %.2f' % (i+1, total))