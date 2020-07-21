def input_dir():
    input_dir = {}
    while True:
        key = input("Key: ")
        if key=="end":
            break
        input_dir[key] = input("Value: ")
    return input_dir

dir_color = input_dir()

for i in sorted(dir_color.keys()):
  print(i,": ",dir_color[i],sep="")