# Write your code here
import random

words = ['python', 'java', 'kotlin', 'javascript']
letters = "abcdefghijklmnopqrstuvwxyz"

def game():
    word = random.choice(words)
    guesses = []
    hidden = "-" * len(word)
    counter = 8
    while hidden != word and counter > 0:
        print()
        print(hidden)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
        elif guess not in letters:
            print("It is not an ASCII lowercase letter")
        elif guess in guesses:
            print("You already typed this letter")
        elif guess in word:
            for char in range(len(word)):
                if guess == word[char]:
                    hidden = hidden[:char] + word[char] + hidden[char + 1:]
        else:
            print("No such letter in the word")
            counter -= 1
        guesses.append(guess)

    if hidden == word:
        print("You guessed the word!\nYou survived!")
    else:
        print("You lost!")

print("H A N G M A N")

while True:
    choice = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if choice != "play":
        break
    game()
