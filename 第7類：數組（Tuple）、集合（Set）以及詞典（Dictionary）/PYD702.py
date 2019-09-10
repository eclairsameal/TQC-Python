# TODO
def input_list():
    lt = []
    while True:
        x = eval(input())
        if(x==-9999):
            break
        lt.append(x)
    return tuple(lt)

print("Create tuple1:")
# TODO
tup1 = input_list()
print("Create tuple2:")
# TODO
tup2 = input_list()
tup3 = tup1 + tup2
print("Combined tuple before sorting:",tup3)
lis = list(tup3)
print("Combined list after sorting:",sorted(lis))