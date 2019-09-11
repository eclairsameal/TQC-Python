# TODO

def input_str():
    str_a = list();
    while True :
        instr = input()
        if(instr == 'end'):
            break
        str_a.append(instr)
        str_a = sorted(str_a)
    return set(str_a)

print("Enter group X's subjects:")
# TODO
x_set = input_str()
print("Enter group Y's subjects:")
# TODO
y_set = input_str()
re_lis = list(x_set | y_set)
print(sorted(re_lis))
re_lis = list(x_set & y_set)
print(sorted(re_lis))
re_lis = list(y_set - x_set)
print(sorted(re_lis))
re_lis = list(x_set ^ y_set)
print(sorted(re_lis))