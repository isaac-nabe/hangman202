# imports random module to be used in code
import random

# creates word list
word_list = ["mango", "banana", "pineapple", "cranberries", "guava"]

# prints word list
# print(word_list)

# randomly selects word from word_list and assigns choice to word variable
word = random.choice(word_list)

# prints random choice from word_list assigned to word variable
# print(word)


# define function to check if the guess is in word
def check_guess(guess):
    """Check if guessed letter is in word."""
    # make guess lowercase
    guess.lower()

    # check if guess is in word
    if guess in word:
        # print message saying guess in word
        print(f"Good Guess! {guess} is in the word!")
    else:
        # print message saying not in the word
        print(f"Sorry, {guess} is not in the word. Try Again.")

# define function to prompt user input until valid guess given


def ask_for_input():
    """Iteravely ask user for input until valid guess is given."""
    # create while loop (ensuring code runs continuously.)
    while True:
        # ask user to guess letter and assign this to variable called guess
        guess = input("Guess a letter: ")
        # check that guess is a *single* alphabetical char.
        if len(guess) == 1 and guess.isalpha():
            # call function to check the guess
            check_guess(guess)
        else:
            # print error message for invalid input
            print("Invalid input. Please, enter a single alphabetical character.")


# call function asking for input
ask_for_input()
