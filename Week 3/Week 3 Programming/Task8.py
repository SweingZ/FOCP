num=int(input("Enter the number required. "))
if num>0:
    for i in range(13):
        print(f"{num} x {i} = {num*i}")
else:
    for i in range(12,-1,-1):
        print(f"{(-1)*num} x {i} = {(-1)*num*i}")