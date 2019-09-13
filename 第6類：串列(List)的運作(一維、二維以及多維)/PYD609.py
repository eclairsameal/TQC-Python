#TODO
#list_a = [[0 for i in range(2)] for i in range(2)]
#list_b = [0, 0, 0, 0]

def input_arr():
    list_a = [[0 for i in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            list_a[i][j] = int(input('[%d, %d]: '%(i+1,j+1)))
    return list_a

def print_arr(li):
    for i in range(2):
        print("**",end='')
        for j in range(2):
            print(li[i][j],end=' ')
        print("**")
    
print("Enter matrix 1:")
li_e = input_arr()

print("Enter matrix 2:")
li_e2 = input_arr()

print("Matrix 1:")
print_arr(li_e)
print("Matrix 2:")
print_arr(li_e2)

print("Sum of 2 matrices:")
for i in range(2):
    print("**",end='')
    for j in range(2):
      print((li_e[i][j]+li_e2[i][j]),end=' ')
    print("**")
