x = int(input())

def compute(x):
    isprime = True
    if x<=1:
        isprime = False
    else:
        for i in range(2, x):    
            if x%i==0:
                isprime = False
    return isprime
if compute(x):
    print("Prime")
else:
    print("Not Prime")
"""
Prime
Not Prime
"""