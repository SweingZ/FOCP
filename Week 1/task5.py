students=int(input("Enter the number of students: "))
if students%24==0:
    groups=students/24
else:
    groups=int(students/24) + 1
print("The number of groups needed is",groups)
print("Number of students in leftover group",students%24)