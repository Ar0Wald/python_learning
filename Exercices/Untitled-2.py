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
    print("\n\n")
    print("Make a choice: ")
    print("1. Sum ")
    print("2. Product")
    print("3. Quotient")
    print("4. Difference")
    choice = input("Enter you choice: ")

    # function to invert numbers in case the 2nd input is higher than the first one
    def invert_numbers(x, y):
        inverted = False
        if y > x:
            x, y = y, x
            inverted = True
        return x, y, inverted

    # loop to allow user to perform another operation
    while True:
        try:
            if choice == "1":
                print(x + y)  # sum
            elif choice == "2":
                print(x * y)  # product
            elif choice == "3":
                print(x / y)  # quotient
            elif choice == "4":
                x, y, inverted = invert_numbers(x, y)
                result = abs(x - y)
                print(result)  # difference
            else:
                while True:
                    print("Invalid choice, please try again")
                    choice = input("Enter you choice: ")
                    if choice in ["1", "2", "3", "4"]:
                        break
                continue

            # Ask user if they want to try again
            answer = input("Do you want to try again? (y/n): ")
            if answer.lower() == "n":
                break  # Exit the loop if user does not want to try again

            # Reset the values for x and y if user wants to try again
            x = 0
            y = 0
            break

        except ValueError:
            print("Error: Please enter a valid choice")
