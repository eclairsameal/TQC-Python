def oneupper(s):
    f = False
    for i in range(len(s)):
        if s[i].isupper():
            f = True
            break
    return f

password = input()
if password.isalnum() and len(password)>=8 and oneupper(password):
    print("Valid password")
else:
  print("Invalid password")