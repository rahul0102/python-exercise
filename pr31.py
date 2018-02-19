# Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess a letter and displays letters
# in the clue word that were guessed correctly. For now, let the player guess an infinite number of times
# until they get the entire word. As a bonus, keep track of the letters the player guessed and display
# a different message if the player tries to guess that letter again. Remember to stop the game when all
# the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of
# the number of guesses the player has remaining

# An example interaction can look like this:
#
# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...

import random
import os
def getRandomWord():
    words = []
    with open('sowpods.txt','r') as f:
        line = f.readline().strip()
        words.append(line)

        while line:
            line = f.readline().strip()
            words.append(line)

    rand_word = random.choice(words).strip()
    return rand_word
def playHangman(guess_letter):
    global guessed_letters
    global guessd_word
    try:
        os.system('clear')
    except:
        pass
    if guess_letter in guessed_letters:
        print("Already Guessed")
        # print(''.join(guessd_word))
    elif guess_letter in word:
        guessed_letters.append(guess_letter)
        # print("guessed_letters: ", guessed_letters)
        for i,w in enumerate(word):
            if w in set(guessed_letters):
                guessd_word[i] = w
    else:
        print("Incorrect")
    print(''.join(guessd_word))
    print()
    return

word = getRandomWord()
guessed_letters = []
guessd_word = list('_' * len(word))

print("=" * 5," Welcome to Hangman! ","=" * 5)
print("Word to guess is : ", word)
while True:

    if '_' in guessd_word:
        guess_letter = input("Guess your letter: ").upper()
        playHangman(guess_letter)
    else:
        print("You Won!")
        break
