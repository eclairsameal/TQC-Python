file = open("write.txt")
for i in range(5):
    file.write(input()+'\n')

file.close()
