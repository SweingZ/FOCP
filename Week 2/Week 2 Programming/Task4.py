sweets=int(input("How many sweets? "))
pupils=int(input("How many pupils? "))
if sweets&pupils==1:
    print("Each student will get",sweets//pupils,"sweets and there will be",sweets%pupils,"sweet left over!")
else:
    print("Each student will get",sweets//pupils,"sweets and there will be",sweets%pupils,"sweets left over!")


