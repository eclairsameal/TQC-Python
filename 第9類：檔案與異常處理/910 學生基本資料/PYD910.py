f_name = "read.dat"
m, f = 0, 0
with open(f_name, "r",encoding="UTF-8") as fp:
    for i in fp:
        print(i)
with open(f_name, "r",encoding="UTF-8") as fp:
    sp_data = fp.read().split(' ')
print(f"Number of males: {sp_data.count('1')}")
print(f"Number of females: {sp_data.count('0')}")
"""
Number of males: _
Number of females: _
"""