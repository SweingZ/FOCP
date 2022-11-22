numbers = [10, 20 , 30]
sum = 0
flag = 0
for i in numbers:
    sum += i
    if sum > 100:
        flag = 1
        break
    print(sum) 
if flag == 0:
    print("All Numbers Processed")
