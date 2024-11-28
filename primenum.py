#ask the user for num
num=int(input("enter a num:"))

#check if it's prime or not
if num<=1:
    print("it is not prime number")
if num >= 2:
    for i in range(2,num):
        if num % i==0:
            print("not prime")
            break
            
    else:
        print(" it is prime")    
       
