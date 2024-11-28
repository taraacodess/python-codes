fruits = {
    "Apple": 130,
    "Avocado" : 50,
    "Sweet Cherries" : 100,
    "Kiwifruit" : 90,
    "Pear" : 100,
}


while True: #runs the program until the input matches the dict above
    item=input("Item:").title() #capitalizes the first letter and make other lower case
    if item in fruits:       #check if the item is in the dict
        print("calories:",fruits[item]) #prints if the item if matches dict 
        break                         # if input matches dict it prints and breaks otherwise it goes again to line 11