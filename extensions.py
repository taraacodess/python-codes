#ask user file's name
name = input("File name:").lower()

#check the type of file

if name.endswith(".jpg"):
    print("image/jpeg")

elif name.endswith(".pdf"):
    print("text/pdf")   

else:
    print("other types of file")   
