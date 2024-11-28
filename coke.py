def coke_machine():
    total_inserted = 0  # Initialize total inserted amount

    while True:  # Continue until we reach or exceed 50
        coin = int(input("Insert a coin (5, 10, or 25): "))

        # Check if the coin is one of the valid values
        if coin in (5, 10, 25):
            total_inserted += coin  # Add the inserted coin to the total
            
            # Check how much is left or if we have enough
            if total_inserted < 50:
                print("Amount due:", 50 - total_inserted)  # Show remaining amount due
            elif total_inserted == 50:
                print("Thank you! You have inserted enough coins.")
                break  # Exit the loop since the amount is exactly 50
            else:  # total_inserted > 50
                excess = total_inserted - 50
                print("Thank you! You have inserted enough coins.")
                print("Returning excess amount:", excess)
                break  # Exit the loop since the amount is more than 50
        else:
            print("Invalid coin. Please insert 5, 10, or 25.")

# Call the function
coke_machine()

 