x = int(input())

if x%3==0 and x%5==0:
    print(x,"is a multiple of 3 and 5.")
elif x%3==0:
    print(x,"is a multiple of 3.")
elif x%5==0:
    print(x,"is a multiple of 5.")
else:
    print(x,"is not a multiple of 3 or 5.")