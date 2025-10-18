 while True:
    print("=====CALCULATOR=====")
    print("Press 'a' for addition")
    print("Press 's' for subtraction")
    print("Press 'm' for multiplication")
    print("Press 'd' for division")
    print("Press 'e' for exit")
    print("====================")

    choice = input("Enter your choice: ")

    if choice == 'a':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, "+", num2, "=", (num1 + num2))

    elif choice == 's':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, "-", num2, "=", (num1 - num2))

    elif choice == 'm':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, "*", num2, "=", (num1 * num2))

    elif choice == 'd':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            print("Second number can't be zero")
        else:
            print(num1, "/", num2, "=", (num1 / num2))

    elif choice == 'e':
        print("Exiting program")
        break

    else:
        print("Invalid choice")

    again = input("Do you wish to calculate again? (y/n): ")
    if again != 'y':
        break
