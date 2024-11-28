#create a list
#sort the value
#store the 



camel_case = input("camelCase: ").strip()

for letter in camel_case:
    if letter.islower():
        print("snake_case:",letter, end="")
    else:
        print("snake_case:","_" + letter.lower(), end="")

print()