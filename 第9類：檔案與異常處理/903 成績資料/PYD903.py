file = open("data.txt", 'a+')

for i in range(5):
    file.write('\n' + input())
print("Append completed!")

file.seek(0, 0)
print('Content of "data.txt":')
print(file.read())

file.close()
