#importing sys module
import sys
count = len(sys.argv)
length = len(sys.argv) - 1
total = 0

#checking if arguments have been passed
if count > 1:
    while count > 1:
        count -= 1
        total += float(sys.argv[count])
    print("Total is", total)
    print("The average is", total/length)

#executes if no arguments have been passed 
else:
    print("No arguments are provided")