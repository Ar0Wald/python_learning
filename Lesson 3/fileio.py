with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("How are you?\n")


with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)