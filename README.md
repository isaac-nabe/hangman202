# Hangman Game

## Table of Contents

1. [Description](#description)
2. [Installation Instructions](#installation-instructions)
3. [Usage Instructions](#usage-instructions)
4. [File Structure](#file-structure)
5. [License](#license)

## Description

## Description
This project implements a simple Hangman game in Python. The objective of the game is for the player to guess a randomly selected word letter by letter. The player has a limited number of lives and loses a life for each incorrect guess. The game ends when the player either guesses the word correctly or runs out of lives.

The aim of this project is to practice object-oriented programming concepts in Python, such as classes, methods, and attributes. Additionally, it involves working with loops, conditionals, and user input handling.

### What I Learned

- How to use the `random` module in Python to select a random element from a list.
- How to handle user input and validate it using conditionals.
- Basic error handling and user feedback.
- Encapsulation and modularization of code using functions.
- How to define and use classes in Python.
- How to manage class attributes and methods.
- How to handle user input and validate it.
- How to implement game logic using loops and conditionals.

## Installation Instructions

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository to your local machine using:
    ```sh
    git clone https://github.com/isaac-nabe/hangman202.git
    ```
3. Navigate to the project directory:
    ```sh
    cd hangman202
    ```

## Usage Instructions

1. Run the script using Python:
    ```sh
    python milestone_4.py
    ```
2. The game will prompt you to guess a letter. You need to input a single alphabetical character. If the guessed letter is in the word, it will be revealed in the word. If not, you will lose a life. The game continues until you either guess the word or run out of lives.

## Example
Guess a letter: a
Good Guess! a is in the word!
Current word: a _ _ _ _

Guess a letter: b
Sorry, b is not in the word. Try Again.
You have 4 lives left.

## File Structure


Hangman202/

├── `milestone_2.py`# Previous draft script.

├── `milestone_3.py# Previous draft script.

├─`milestone_4.py`# Main script containing the Hangman class and game logic

├── `README.md`


- `milestone_2.py`: The main script file containing the *draft* game logic for the second milestone.
- `milestone_3.py`: Contains the refactored code for the third milestone. This file contains a more developed hangman concept.
- `milestone_4.py`: 
- `README.md`: This README file containing project information and instructions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

