y = int(input())
if y % 4 ==0 and y % 100 != 0 or y % 400 == 0:
    print("{} is a leap year.".format(y))
else :
    print("{} is not a leap year.".format(y))

    
# version: elif
year = int(input('Please input year:'))

if( year % 400 == 0):
    print('{} is a leap year.'.format(year))
elif( year % 100 == 0):
    print('{} is a normal year.'.format(year))
elif( year % 4 == 0):
    print('{} is a leap year.'.format(year))
else:
    print('{} is a normal year.'.format(year))

    
# version: nest if
year = int(input('Please input year:'))

if( year % 400 == 0):
    print('{} is a leap year.'.format(year))
else:
    if( year % 100 == 0):
        print('{} is a normal year.'.format(year))
    else:
        if( year % 4 == 0):
            print('{} is a leap year.'.format(year))
        else:
            print('{} is a normal year.'.format(year))
            

            
