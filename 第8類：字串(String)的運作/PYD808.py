ssn_list = input().split('-')

flag = True
for i in range(len(ssn_list)):
    if not ssn_list[i].isdigit():
        print('Invalid SSN')
        flag = False
if flag == True:
    print('Valid SSN')