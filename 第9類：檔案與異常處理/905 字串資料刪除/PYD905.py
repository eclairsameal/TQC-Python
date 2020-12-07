f_name = input()
string = input()
fp = open(f_name, 'r+')
datas = fp.read()

print("=== Before the deletion")
print(datas)

print("=== After the deletion")
datas = datas.replace(string, "")
print(datas)

fp.seek(0)
fp.write(datas)
fp.close()
