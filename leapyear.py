#ask user to enter a year

yr=int(input("enter a year:"))

#check and print if it's a leap year

if yr % 4 == 0 and yr :
    print("it is a lear year")

elif yr % 400 == 0 and yr % 100==0:
    print("it is a leap year")

else:
    print("it is not a leap year")    