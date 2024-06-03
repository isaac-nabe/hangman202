# fine contains code for final game

import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game attributes.

        Parameters:
        - word_list (list): A list of words to pick the word to be guessed from.
        - num_lives (int): The number of lives the player has at the start of the game. Default is 5.
        """
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def _update_word_guessed(self, guess):
        """Update the word_guessed list with the guessed letter."""
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word!")
            self._update_word_guessed(guess)
            self.num_letters -= self.word.count(guess)
            print(f"Current word: {' '.join(self.word_guessed)}")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Continuously ask the user for input until a valid guess is given."""
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


def play_game(word_list):
    """
    Function to play the Hangman game.

    Parameters:
    - word_list (list): A list of words to pick the word to be guessed from.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif '_' not in game.word_guessed:
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()


if __name__ == "__main__":
    word_list = ["mango", "banana", "pineapple", "cranberries", "guava"]
    play_game(word_list)
