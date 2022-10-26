students=int(input("How many students? "))
size=int(input("Required group size? "))
if students&size==1:
    print("There will be",students//size,"groups and there will be",students%size,"student left over!")
else:
    print("There will be",students//size,"groups and there will be",students%size,"students left over!")