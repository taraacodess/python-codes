def factorial():
    s=int(input("enter a number"))
    for i in range(1,s+1):
        if s % i == 0:
            print(i,end=",")

factorial()            
    