# TODO
s = set()
while True :
    x = int(input())
    if(x == -9999):
        break
    s.add(x)
print('Length:', len(s))
print('Max:', max(s))
print('Min:', min(s))
print('Sum:', sum(s))