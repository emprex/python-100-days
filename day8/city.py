prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' to end the program. "
while True:
    city = input(prompt)
    if city.lower() == 'quit':
        break
    else:
        print(f"You have visited {city}.")

