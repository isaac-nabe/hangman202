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
        self.word_list = word_list  # List of words from which the word to be guessed is chosen
        self.word = random.choice(word_list)  # The word to be guessed, chosen randomly from word_list
        self.word_guessed = ['_' for _ in self.word]  # List representing the guessed word, '_' for unguessed letters
        self.num_letters = len(set(self.word))  # Number of unique letters in word, not guessed yet
        self.num_lives = num_lives  # Number of lives the player has at the start of the game
        self.list_of_guesses = []  # List of guesses that have already been tried

    def _update_word_guessed(self, guess):
        """
        Update the word_guessed list with the guessed letter.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        for index, letter in enumerate(self.word):  # Iterate over the word with both index and letter
            if letter == guess:  # If the current letter matches the guessed letter
                self.word_guessed[index] = guess  # Replace the corresponding '_' in word_guessed with the guessed letter

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        guess = guess.lower()  # Convert the guessed letter to lowercase
        if guess in self.word:  # If the guessed letter is in the word
            if guess not in self.list_of_guesses:  # If the guessed letter has not been guessed before
                print(f"Good guess! {guess} is in the word!")
                self._update_word_guessed(guess)  # Update the word_guessed list with the guessed letter
                self.num_letters -= 1  # Decrement the count of unique letters left to guess
                print(f"Current word: {' '.join(self.word_guessed)}")
            else:
                print(f"You already guessed the letter {guess}.")
        else:
            self.num_lives -= 1  # Decrement the number of lives
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Continuously ask the user for input until a valid guess is given.
        """
        while True:
            guess = input("Guess a letter: ")  # Prompt the user to guess a letter
            if len(guess) != 1 or not guess.isalpha():  # Check if the input is a single alphabetical character
                print("Invalid input. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:  # Check if the letter has already been guessed
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  # Check if the guessed letter is in the word
                self.list_of_guesses.append(guess)  # Append the guessed letter to the list of guesses
                break

def play_game(word_list):
    """
    Function to play the Hangman game.

    Parameters:
    - word_list (list): A list of words to pick the word to be guessed from.
    """
    game = Hangman(word_list)  # Create an instance of the Hangman class

    while True:
        if game.num_lives == 0:  # Check if the player has run out of lives
            print('You lost!')
            break
        elif game.num_letters == 0:  # Check if the player has guessed all unique letters
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()  # Ask for the player's input
        print(f"Debug: num_lives={game.num_lives}, num_letters={game.num_letters}, word_guessed={''.join(game.word_guessed)}")  # Print debug information

if __name__ == "__main__":
    word_list = ["mango", "banana", "pineapple", "cranberries", "guava"]  # List of words for the game
    play_game(word_list)  # Start the game
