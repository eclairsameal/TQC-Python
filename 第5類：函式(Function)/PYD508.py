(x,y)=eval(input())
def compute(x,y):
    while(x!=0):
        x=x%y
        y=y-x
    return y
print(compute(x,y))