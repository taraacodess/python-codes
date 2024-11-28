#ask user enter a number
num= int (input("enter a number:"))
#check if it's a prime number or not
if num<=1:
    print("it is not a prime number")
if num>=2:
    for i in range(2,num):
        if num % i == 0:
            print("it is not a prime number")
            break
        else:
            print("it is a prime number")    
        