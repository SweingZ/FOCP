while 1:
    pw=input("Enter a password: ")
    pwd=input("Enter the password again: ")
    if pw == pwd:
        print("Password set")
        break
    else:
        print("Password is wrong!!!")