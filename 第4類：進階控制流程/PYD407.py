while True:
    year = eval(input())  
    if year==-9999:
        break
    if year%4==0 and year%100!=0:
        print("{:d} is a leap year.".format(year))
    elif year%400==0:
        print("{:d} is a leap year.".format(year))
    else:
        print("{:d} is not a leap year.".format(year))
"""
_ is a leap year.
_ is not a leap year.
"""
