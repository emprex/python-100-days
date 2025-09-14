"""Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza."""

prompt = "\nPlease enter a pizza topping (or 'quit' to finish): "
while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        print("Finished adding toppings.")
        break
    else:
        print(f"Adding {topping} to your pizza.")