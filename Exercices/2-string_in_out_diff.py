while True:
# Input two numbers.
# as long as two inputs are not floating numbers, print an error message
    while True:
        try:
            x = float(input("Enter 1st number: "))
            y = float(input("Enter 2nd number: ")) 
            break  
        except ValueError:
            print("Error: Please enter a valid number")

# Menu for making choice
    print("")
    print("")
    print("Make a choice: ")
    print("1. + ")
    print("2. *")
    print("3. /")
    print("4. Difference")
    choice = input("Enter you choice: ")


# function to invert numbers in case the 2nd input is higer than the first one
# not used in the script but good to know
    def invert_numbers (x, y):
        inverted = False
        if y > x:
            x, y = y, x
            inverted = True
        return x, y, inverted

# Different possible results
    exit_the_script = False
    while not exit_the_script:
        try:
            if choice == "1":
                print(x + y)      # Sum
            elif choice == "2":
                print(x * y)     # Product
            elif choice == "3":
                print(x / y)     # Quotient
            elif choice == "4":   
                print(abs(x - y))  # Difference                            
            else:
                while True:
                    print("Invalid choice, please try again")
                    choice = input("Enter you choice: ")
                    if choice in ["1", "2", "3", "4"]:
                        break 
                continue
        
        # Wait for user input before exiting the script
            answer = input("Do you want to try again? (y/n): ")
            if answer.lower() == "n":
                exit_the_script = True
            else:
            
            # Reset the values if you want to try again because entire code is wrapped inside a while loop
                x = 0
                y = 0
                break

        except ValueError:
            print("Error: Please enter a valid choice")
    
    if exit_the_script:
        break
        