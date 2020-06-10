def compute(p,q):
    while(p!=0):
        p=p%q
        q=q-p
    return q
(x,y)=eval(input())
(m,n)=eval(input())

p = x*n + y*m
q = y*n

print("{}/{} + {}/{} = {}/{}".format(x, y, m, n, int(p/compute(p, q)), int(q/compute(p, q))))