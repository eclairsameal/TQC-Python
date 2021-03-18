"""
def compute(s, c):
    count_c = 0
    for x in s:
        if x == c:
            count_c+=1
    return count_c
"""

def compute(s, c):
    return s.count(c)
    
string = input()
c = input()
print("{:s} occurs {:d} time(s)".format(c, compute(string, c)))
