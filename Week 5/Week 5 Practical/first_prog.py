#taking input from user
number = input("Enter a number: ")

#converting input into int data type
number = int(number)

#printing the entered number
print("The numbered entered was", number)

#checking if the number is even
if (number % 2) == 0:
    print("That is an even number")
    if (number%10) == 0:
        print("It is divisible by ten")
    else:
        print("It is not dividible by ten")

#this statement executes only if the number is odd
else:
    print("That is an odd number")
    print("It is not divisible by ten")