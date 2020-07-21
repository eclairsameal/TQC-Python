def input_num(n):
    g_sum = 0
    print("The {:d}st student:".format(n))
    for i in range(5):
        g_sum+=int(input())
    return g_sum

grades_list = []
for i in range(3):
    grades_list.append(input_num(i + 1))

for i in range(3):
    print("Student {:d}".format(i+1))
    print("#Sum {:d}".format(grades_list[i]))
    print("#Average  {:.2f}".format(grades_list[i]/5))
"""
The _ student:
Student _
#Sum _
#Average _
"""
