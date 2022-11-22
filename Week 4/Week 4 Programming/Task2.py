def string_check(user_input):
    upper = 0
    lower = 0
    digit = 0
    for i in user_input:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digit += 1
    print(f"{upper},{lower},{digit}")

string_check("Ab1")