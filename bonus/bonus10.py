try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        # it will interrupt the program and print the String in red
        exit("That looks like a square")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")