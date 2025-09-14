prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "Enter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message.lower() != 'quit':
        active = False
    else:
        print(f"You said: {message}")
############################

name = input("Please enter your name: ")
print(f"Hello, {name}! It's nice to meet you.")

############################

prompt = "If you tell me who you are, I can personalize your message. "
prompt += "What is your name? "

name = input(prompt)
age = int(input("How old are you? "))
print(f"Hello, {name}! You are {age} years old.")
print(age >= 18)



