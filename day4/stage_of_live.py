while True:
    # Input validation loop
    while True:
        try:
            age = int(input("Insert your age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"Your age is: {age} years old")

    if age < 2:
        print("You are a baby")
    elif age >= 2 and age < 4:
        print("You are a toddler")
    elif age >= 4 and age < 13:
        print("You are a kid")
    elif age >= 13 and age < 20:
        print("You are a teenager")
    elif age >= 20 and age < 65:
        print("You are an adult")
    else:
        print("You are an elder")

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
