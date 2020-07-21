n_l = []
for i in range(9):
    n_l.append(int(input()))

max_n = max(n_l)  
print("Index of the largest number {} is: ({}, {})"
      .format(max_n, n_l.index(max_n)//3, n_l.index(max_n)%3))

min_n = min(n_l)
print("Index of the smallest number {} is: ({}, {})"
      .format(min_n, n_l.index(min_n)//3, n_l.index(min_n)%3))
"""
Index of the largest number _ is: (_, _)
Index of the smallest number _ is: (_, _)
"""