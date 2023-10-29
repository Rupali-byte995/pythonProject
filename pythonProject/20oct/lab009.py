# match
number = int(input("Enter the number you want to enter"))
match number:
    case 1:
        print("You entered 1")
    case 2:
        print("You entered 2")
    case _:
        print("I have no idea")
