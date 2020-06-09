nami = 0
chopper = 0
null_vote = 0
for i in range(5):
    vote = int(input())
    if vote == 1:
        nami+=1
    elif vote == 2:
        chopper+=1
    else:
        null_vote+=1
    print("Total votes of No.1: Nami =  {}".format(nami))
    print("Total votes of No.2: Chopper =  {}".format(chopper))
    print("Total null votes =  {}".format(null_vote))
if nami > chopper:
    print("=> No.1 Nami won the election.")
elif nami < chopper:
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")   
"""
Total votes of No.1: Nami =  _
Total votes of No.2: Chopper =  _
Total null votes =  _

=> No.1 Nami won the election.
=> No.2 Chopper won the election.
=> No one won the election.
"""
