# voting.py

age = int(input("What is your age? "))
if age >= 18:
    print("You are old enough to vote!")
    print("have you resistered to vote yest?")

else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18")

# amusement.py

age = int(input("What is your age? "))

if age < 4:
    print("Your admission cost is $0.")

elif age < 18:
    print("Your admission cost is $25.")

else:
    print("Your admission cost is $40")

# amusemet2.py

age = int(input("What is your age? "))

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")






