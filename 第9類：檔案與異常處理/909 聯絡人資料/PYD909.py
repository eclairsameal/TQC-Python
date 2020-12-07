f_name = "data.dat"
with open(f_name, "w",encoding="UTF-8") as fp:
    for i in range(5):
        fp.write(input() + "\n")
print('The content of "data.dat":')    
with open(f_name, "r",encoding="UTF-8") as fp:
  for i in fp:
      print(i)
"""
The content of "data.dat":
"""