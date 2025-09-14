"""A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket."""

prompt = "Please enter your age (or 'quit' to exit): "
while True:
    age_input = input(prompt)
    if age_input.lower() == 'quit':
        print("Thank you for using the ticket price calculator.")
        break
    try:
        age = int(age_input)
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
    except ValueError:
        print("Please enter a valid age or 'quit' to exit.")