# Goal: Build a command-line calculator that can add, subtract, multiply, or divide two numbers.
while True:
# Ask the user to enter two numbers

    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

# Ask the user to enter the operator

    operator = input("Enter operation (+, -, *, /) ")

# operation

    if operator == '+':
        result = num1 + num2

    elif operator == '-':
        result = num1 - num2

    elif operator == '*':
        result = num1 * num2

    elif operator == '/':
        if num2 == 0:
            result = "Error: Division by zero"
        else: result = num1 /num2

    else:
        result = "Invalid operator: "

    print(result)

    again = input("Continue? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break

