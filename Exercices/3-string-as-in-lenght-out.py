# ANSI escape codes for text color
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

while True:
    exit_script = False
    while not exit_script:
        message =  input("Write your message here: ")
        string_lenght = len(message)
        print("Your message has: ", GREEN + str(string_lenght) + RESET ," characters")
        print("")
        try:
            while True:
                choice = input("Do you want to write another message? (y/n):  ")
                if choice.lower() in ["No", "n", "no"]:
                    exit_script = True
                    break
                elif choice.lower() in ["Yes", "y", "yes"]:
                    message = ""
                    string_lenght = ""
                    break
                else:
                    print("Answer must be either Yes or no")
                    continue
        except ValueError:
            print("Please enter a valid input")
    if exit_script:
        break
else: 
    exit