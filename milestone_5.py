import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game attributes.

        Parameters:
        - word_list (list): A list of words to pick the word to be guessed from.
        - num_lives (int): The number of lives the player has at the start of the game. Default is 5.
        """
        # Hangman attributes
        # List of words from which the word to be guessed is chosen
        self.word_list = word_list
        # The word to be guessed, chosen randomly from word_list
        self.word = random.choice(word_list)
        # List representing the guessed word, '_' for unguessed letters
        self.word_guessed = ['_' for _ in self.word]
        # Number of unique letters in word, not guessed yet
        self.num_letters = len(set(self.word))
        # Number of lives the player has at the start of the game
        self.num_lives = num_lives
        # List of guesses that have already been tried
        self.list_of_guesses = []

    # Hangman Methods
    # _update_word_guessed() is for internal use
    def _update_word_guessed(self, guess):
        """
        Update the word_guessed list with the guessed letter.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        # Iterate over the word with both index and letter
        for index, letter in enumerate(self.word):
            # If the current letter matches the guessed letter
            if letter == guess:
                # Replace the corresponding '_' in word_guessed with the guessed letter
                self.word_guessed[index] = guess

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        # Convert the guessed letter to lowercase
        guess = guess.lower()
        # If the guessed letter is in the word
        if guess in self.word:
            # If the guessed letter has not been guessed before
            if guess not in self.list_of_guesses:
                print(f"Good guess! {guess} is in the word!")
                # Update the word_guessed list with the guessed letter --> this was where old bug was
                self._update_word_guessed(guess)
                # Decrement the count of unique letters left to guess --> also where old bug was
                self.num_letters -= 1
                print(f"Current word: {' '.join(self.word_guessed)}")
            else:
                print(f"You already guessed the letter {guess}.")
        else:
            # Decrement the number of lives
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Continuously ask the user for input until a valid guess is given.
        """
        while True:
            # Prompt the user to guess a letter
            guess = input("Guess a letter: ")
            # Check if the input is a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please, enter a single alphabetical character.")
            # Check if the letter has already been guessed
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Check if the guessed letter is in the word
                self.check_guess(guess)
                # Append the guessed letter to the list of guesses
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    """
    Function to play the Hangman game.

    Parameters:
    - word_list (list): A list of words to pick the word to be guessed from.
    """
    # Create an instance of the Hangman class
    game = Hangman(word_list)

    while True:
        # Check if the player has run out of lives
        if game.num_lives == 0:
            print('You lost!')
            break
        # Check if the player has guessed all unique letters
        elif game.num_letters == 0:
            print('Congratulations. You won the game!')
            break
        else:
            # Ask for the player's input
            game.ask_for_input()
        # Print debug information
        print(f"Debug: num_lives={game.num_lives}, num_letters={
              game.num_letters}, word_guessed={''.join(game.word_guessed)}")


if __name__ == "__main__":
    # List of words for the game
    word_list = ["mango", "banana", "pineapple", "cranberries", "guava"]
    # Start the game
    play_game(word_list)
