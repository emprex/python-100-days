
import random  # to generate random numbers

def guessing_game():
    # Game logic: a simple number guessing game between 1 and 20
    number_to_guess = random.randint(1, 20)
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low, try again.")
            elif guess > number_to_guess:
                print("Too high, try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # <-- Only break when the guess is correct!
        except ValueError:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    guessing_game()
