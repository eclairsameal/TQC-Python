y = int(input())
if y % 4 ==0 and y % 100 != 0 or y % 400 == 0:
    print("{} is a leap year.".format(y))
else :
    print("{} is not a leap year.".format(y))
