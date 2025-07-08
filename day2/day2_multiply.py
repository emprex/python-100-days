# define a function that multiply two numbers

def multiply(a, b):
    product = a * b
    return product

# Main fuction who ask users for 2 values and call the function and print the result

if __name__ == "__main__":
    while True: 
        try:
            x = int(input("please insert value 1: "))
            break

        except ValueError:
            print("Invalid input!. Please enter a valid integer:")
    while True:
        try:
            y = int(input("Please insert value 2: "))
            break
        
        except ValueError:
            print("Invalid input!. Please enter a valid integer:")
    
    result = multiply(x, y)
    print(result)
