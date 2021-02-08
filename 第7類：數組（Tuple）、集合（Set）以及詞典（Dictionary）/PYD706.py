k = int(input())

for i in range(k):
    instr = input()
    instr = instr.lower()
    instr = instr.replace(' ', '')
    instr = set(instr)
    print(len(instr) == 26)
