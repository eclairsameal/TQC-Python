# TODO

char = input()
if char.isalpha():
    print(char,"is an alphabet.")
elif char.isdigit():
    print(char,"is a number.")
else:
    print(char,"is a symbol.")

    
char = input()
if str.isalpha(char):
    print("{} is an alphabet.".format(char))
elif str.isdigit(char):
    print("{} is a number.".format(char))
else:
    print("{} is a symbol.".format(char))
"""
_ is an alphabet.
_ is a number.
_ is a symbol.
"""
