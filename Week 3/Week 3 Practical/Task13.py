numbers = [10, 20 , 30, 90, 200, 30, 22, 11]
sum = 0
for i in numbers:
    sum += i
    if sum > 100:
        break
    print(sum) 
