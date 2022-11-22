while 1:
    pw=input("Enter a password: ")
    if 8<=len(pw)<=12:
        pwd=input("Enter the password again: ")
        if pw == pwd:
            print("Password set")
            break
        else:
            print("Password is wrong!!!")
    else:
        print("Password is not long enough!!!")