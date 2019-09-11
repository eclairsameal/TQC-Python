# TODO
k = int(input())
str_abc = set('abcdefghijklmnopqrstuvwxyz')
for i in range(k):
    instr = input()
    instr = instr.lower()
    instr = instr.replace(' ', '')
    instr = set(instr)
    print(str_abc == instr)