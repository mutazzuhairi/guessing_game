import random
from utility import Utility

# Lower and Upper bounds
LOWER, UPPER = 1, 100


def new_game():
    # generating random number between
    # the lower and upper
    target_number = random.randint(LOWER, UPPER)

    # Initializing the number of guesses.
    count = 0

    # for calculation of minimum number of
    # guesses depends upon range
    while True:
        count += 1

        # taking guessing number as input
        input_value = input("Guess a number:- ")
        is_input_valid = Utility.check_is_guessing_input_valid(input_value, UPPER, LOWER)
        if not is_input_valid:
            print("Please insert a valid number between 1 and 100 ...")
            continue
        guess = int(input_value)

        # Condition testing
        if target_number == guess:
            print("Congratulations you did it in ", count, " try")
            # Once guessed, loop will break
            break
        elif target_number > guess:
            print("You guessed too small!")
        elif target_number < guess:
            print("You Guessed too high!")


if __name__ == '__main__':
    new_game()
