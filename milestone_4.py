# file contains code for the third milestone.

# import random
import random

# define class


class Hangman:
    # class constructor
    def __init__(self, word_list, num_lives=5):
        """
        Ititialise the Hangman game attributes.

        Parameters:
        - word_list (list): A list of words that the word to be guessed is picked.
        - num_lives (int): The number of lives the player has at the start of the game. Default = 5.
        """
        # Attributes
        self.word_list = word_list  # list of words from which word to be guessed is chosen
        # The word to be guessed, chosen randomly from word_list
        self.word = random.choice(word_list)
        # List representing the guessed word, '_' for unguessed letters
        self.word_guessed = ['_' for _ in self.word]
        # number of unique letters in word, not guessed yet. len() for num letters, set() for UNIQUE letters not guessed yet
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives  # number of lives players have at start of game
        self.list_of_guesses = []  # list of guesses that have been tried

    # Methods
        # define function to check if the guess is in word
    def check_guess(self, guess):
        """Check if guessed letter is in word."""
        # make guess lowercase with .lower() & assign that to guess variable to update
        guess = guess.lower()

        # check if guess is in word
        if guess in self.word:
            # print message saying guess in word
            print(f"Good Guess! {guess} is in the word!")
            # add for loop to replace underscores with guessed letter
            # Iterate over the word with both index and letter
            for index, letter in enumerate(self.word):
                # if letter is equal to guess...
                if letter == guess:
                    # Replace the corresponding "_" in word_guessed with the guessed letter
                    self.word_guessed[index] = guess
            # reduce num_letters by 1 for each occurance of guessed letter in word
            self.num_letters -= self.word.count(guess)
            # print the current state of word_guessed
            print(f"Current word: {' '.join(self.word_guessed)}")
        else:
            # reduce 'num_lives' by 1
            self.num_lives -= 1
            # print message saying not in the word
            print(f"Sorry, {guess} is not in the word. Try Again.")
            # print number of lives left message
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Iteravely ask user for input until valid guess is given."""
        # create while loop (ensuring code runs continuously.)
        while True:
            # ask user to guess letter and assign this to variable called guess
            guess = input("Guess a letter: ")
            # check that guess is a *single* alphabetical char.
            if len(guess) != 1 or not guess.isalpha():
                # print error message for invalid input
                print("Invalid input. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # call function to check the guess
                self.check_guess(guess)
                # append guess to list of guesses
                self.list_of_guesses.append(guess)


# Creating an instance of Hangman, and calling ask_for_input
if __name__ == "__main__":
    # creates word list
    word_list = ["mango", "banana", "pineapple", "cranberries", "guava"]

    # create instance of Hangman class, in this case 'instance' = game
    game = Hangman(word_list)

    # call ask_for_input method on 'game' instance
    game.ask_for_input()
