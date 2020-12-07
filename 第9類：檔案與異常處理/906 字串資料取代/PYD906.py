f_name = input()
str_old = input()
str_new = input()
fp = open(f_name, "r+")
data = fp.read()

print("=== Before the replacement")
print(data)

print("=== After the replacement")
data = data.replace(str_old, str_new)
print(data)

fp.seek(0)
fp.write(datas)
fp.close()
