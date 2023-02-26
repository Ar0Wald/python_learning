# ANSI escape codes for text color
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

while True:
    exit_script = False
    while not exit_script: 
        name = input("What is your name? ")
        cus_message = input("Type a custom message: ")
        print("Greetings", GREEN + name + RESET,"here is your custom message:", YELLOW + cus_message + RESET)
        print("")
        choice = input("Do you want to write another message? (y/n): ")
        if choice.lower() == "n":
            exit_script = True
            break
        
        else:
            name = ""
            cus_message = ""
            break
    
    if exit_script:
        break
else:
    exit