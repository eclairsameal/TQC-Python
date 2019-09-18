str = input()
sum = 0
for i in range(len(str)) :
    print("ASCII code for '{}' is {}".format(str[i], ord(str[i])))
    sum+=ord(str[i])
print(sum)