#ask user what is the great question
qtn=input("what is the answer to the  Great Question of Life, the Universe and Everything?").lower().strip()

if qtn== '42' or qtn=='forty two' or qtn=='forty-two':
    print("yes")
else:
    print("no")    