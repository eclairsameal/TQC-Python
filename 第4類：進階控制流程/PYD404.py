s=input()
print(s[::-1])


s = int(input())
while s > 0:
    print(s % 10, end = "")
    s//=10
