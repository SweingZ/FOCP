BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while 1:
    pw=input("Enter a password: ")
    if 8<=len(pw)<=12 and pw not in BAD_PASSWORDS:
        pwd=input("Enter the password again: ")
        if pw == pwd:
            print("Password set")
            break
        else:
            print("Password is wrong!!!")
    else:
        print("Enter a safer password")