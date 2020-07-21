def compute(s, c):
    return s.count(c)
    
string = input()
c = input()
print("{:s} occurs {:d} time(s)".format(c, compute(string, c)))