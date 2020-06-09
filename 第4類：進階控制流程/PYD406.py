import math
while True:
    h = eval(input())  
    if h==-9999:
        break
    w = eval(input())
    bmi = w/ math.pow(h/100,2.0)
    print("BMI: {:.2f}".format(bmi))
    if bmi < 18.5:
        print("State: under weight")
    elif bmi < 25:
        print("State: normal")
    elif bmi < 30:
        print("State: over weight")
    else:
        print("State: fat")
"""
fat
over weight
normal
under weight
BMI: _
State: _
"""