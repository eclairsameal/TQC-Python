# TODO

def input_n(n):
    s = set()
    for i in range(n):
        x = int(input())
        s.add(x)
    return s
print("Input to set1:")
# TODO
set1 = input_n(5)
print("Input to set2:")
# TODO
set2 = input_n(3)
print("Input to set3:")
# TODO
set3 = input_n(9)

print("set2 is subset of set1:",set2.issubset(set1))
print("set3 is superset of set1:",set3.issuperset(set1))