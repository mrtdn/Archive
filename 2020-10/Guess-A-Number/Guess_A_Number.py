# Abdullah Mert Dinçer
# b2200356016
# 6-October-2020

import random

# Generates a random number between 0 and 100
random_number = random.randint(0, 100)


# This function simply compare two variables which are random_number and guessed_number
def run_guess_game():
    # If user does not supply an integer value program will return an error message. To prevent this I used try-except blocks...
    # ... If user does provide a value something that is not integer program will jump to except block.
    try:
        guessed_number = -1                             # I initialized the guessed_number with a value different from the interval that I will use
        while guessed_number != random_number:          # Here is a loop if user's number is not equal to random number, this block will be executed again and again.
            guessed_number = int(input("Please enter a number between 0 and 100. (Both lower and upper limits are included): "))
            if guessed_number in range(0, 101):         # I used this if block to make sure the number that user chose is in the range 0 and 100
                if guessed_number > random_number:
                    print("Unfortunately it is wrong! Try something smaller.")
                elif guessed_number < random_number:
                    print("Unfortunately it is wrong! Try something bigger.")
                else:
                    print("You found it! Congratulations!")
                    break                               # If user finds the right value program halts.
            else:
                print("Enter a number between 0 and 100!")
    except:
        print("Enter a number between 0 and 100!")     # If user tries to enter a value that's not integer program warns him/her and halts.


run_guess_game()                                       # Calling function