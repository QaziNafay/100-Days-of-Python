import random

import hangman_words
from hangman_art import stages
from hangman_art import logo

print(logo)


words = [hangman_words.word_list]

randomword = random.choice(hangman_words.word_list)

lives = 6
correctletter = []

blank = ""
wordlength = len(randomword)
for length in range(wordlength):
    blank += "_"
print(blank)


gameover = False
while not gameover:

    guess = input("Guess the word:\n").lower()

    if guess in correctletter:
        print(f"You have already guessed the letter {guess}")

    reveal = ""

    if guess not in randomword:
        lives -= 1
        print(f"The letter you chose '{guess}' is incorrect. \nRemaining lives: ", lives)

    if lives == 0:
        print(stages[lives])
        gameover = True
        print("You lose.")
        try_again = input("Try again? (y/n)\n").lower()
        if try_again == "y":
            gameover = False
            randomword = random.choice(words)
            lives = 6

        elif try_again == "n":
            print("Thank you for playing hangman")
        else:
            print("Invalid Response")

    for letter in randomword:
        if letter == guess:
            reveal += letter
            correctletter.append(guess)

        elif letter in correctletter:
            reveal += letter

        else:
            reveal += "_"

    if "_" not in reveal:
        gameover = True
        print("You win.")
        print(f"The word was: {randomword}")


    print(reveal)
    print(stages[lives])