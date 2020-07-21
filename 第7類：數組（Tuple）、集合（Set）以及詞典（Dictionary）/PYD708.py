def input_dir():
    input_dir = {}
    while True:
        key = input("Key: ")
        if key=="end":
            break
        input_dir[key] = input("Value: ")
    
    return input_dir

print('Create dict1:')
dir_1 = input_dir()
print('Create dict2:')
dir_2 = input_dir()

dir_1.update(dir_2)
for i in sorted(dir_1.keys()):
  print(i,": ",dir_1[i],sep="")
