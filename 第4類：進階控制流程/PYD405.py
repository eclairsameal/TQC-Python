while True:
    g = eval(input())
    if g==-9999:
        break
    if g>=90:
        print("A")
    elif g>=80:
        print("B")
    elif g>=70:
        print("C")
    elif g>=60:
        print("D")
    else:
        print("E")