x = int(input())
min = x
for i in range(9):
    x = int(input())
    if x < min:
        min = x
print(min)