import random

colors = ['green', 'yellow', 'red']


point = 0
while True :

    alien_color = random.choice(colors)

    print(f"the alien color is: {alien_color}")

    if alien_color == 'green':
        print("the player just earned 5 points")
        point += 5
    elif alien_color == 'yellow':
        print("the player just earned 10 points")
        point += 10
    elif alien_color == 'red':
        print("the player just earned 15 points")
        point += 15
    else:
        print("no point this round")
    
    print(f"Total points: {point}")

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")  

        break

