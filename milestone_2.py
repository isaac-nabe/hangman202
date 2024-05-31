# imports random module to be used in code
import random

# creates word list
word_list = ["mango", "banana", "pineapple", "cranberries", "guava"]

# prints word list
print(word_list)

# randomly selects word from word_list and assigns to word variable
word = random.choice(word_list)

# prints random choice from word_list assigned to word variable
print(word)

# prompts user for single letter & takes input, assigns to guess variable
guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
