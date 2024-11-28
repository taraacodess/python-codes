# Define the function
def calc_exp():
    # Ask for user input
    x, y, z = input("Enter expression (e.g., '3 + 4'): ").split()
    
    # Convert x and z to integers
    x = int(x)
    z = int(z)
    
    # Perform the calculation based on the operator
    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "/":
        print(x / z)
    elif y == "*":
        print(x * z)
    else:
        print("Invalid operator")

# Call the function
calc_exp()
