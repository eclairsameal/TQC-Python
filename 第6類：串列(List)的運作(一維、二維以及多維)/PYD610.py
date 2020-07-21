t = []
for i in range(1,5):
    print("Week {:d}:".format(i))
    for j in range(1,4):
        t.append(eval(input("Day {:d}:".format(j))))

t_average = sum(t)/len(t)
print("Average: {:.2f}".format(t_average))
print("Highest: {:.2f}".format(max(t)))
print("Lowest: {:.2f}".format(min(t)))

"""
Week _:
Day _: 
Average: _
Highest: _
Lowest: _
"""