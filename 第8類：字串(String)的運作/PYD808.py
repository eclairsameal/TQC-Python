ssn_list = input().split('-')
'''
# index
if ssn_list[0].isdigit() and ssn_list[1].isdigit() and ssn_list[2].isdigit():
    print('Valid SSN')
else:
    print('Invalid SSN')
'''
'''
# flag
flag = True
for i in range(len(ssn_list)):
    if not ssn_list[i].isdigit():
        print('Invalid SSN')
        flag = False
if flag == True:
    print('Valid SSN')
'''    
# for else
for i in range(len(ssn_list)):
    if not ssn_list[i].isdigit():
        print('Invalid SSN')
        break
else:
    print('Valid SSN')
