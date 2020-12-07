"""
Average height: _
Average weight: _
The tallest is _ with _cm
The heaviest is _ with _kg
"""
data, name, height, weight = [], [], [], []

fp=open('read.txt','r',encoding='UTF-8')
for line in fp:  
    print(line)   
    data = (line.replace('\n', ' ').split(' ')) # 將每行字串切割成串列
    name.append(data[0])
    height.append(int(data[1]))
    weight.append(int(data[2]))
fp.close()
print("Average height: {:.2f}".format(sum(height)/len(height)))
print("Average weight: {:.2f}".format(sum(weight)/len(weight)))
tallest_i = height.index(max(height))
print("The tallest is {} with {:.2f}cm".format(name[tallest_i], height[tallest_i]))
heaviest_i = weight.index(max(weight))
print("The heaviest is {} with {:.2f}kg".format(name[heaviest_i], weight[heaviest_i]))
