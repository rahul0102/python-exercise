# finish building Hangman. In the game of Hangman,
# the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

import random
import os

def printHang(n):
    gal = [['---- '],
           ['|  | '],
           ['|    '],
           ['|    '],
           ['|    ']]
    if n < 6:
        gal[2] = ['|  o ']
    if n < 5:
        gal[3] = ['| /  ']
    if n < 4:
        gal[3] = ['| / \\']
    if n < 3:
        gal[3] = ['| /|\\']
    if n < 2:
        gal[4] = ['| /  ']
    if n < 1:
        gal[4] = ['| / \\']
    for i in gal:
        print(''.join(i))

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
    global guess_count
    try:
        os.system('clear')
    except:
        pass

    if guess_letter in guessed_letters:
        print("Already Guessed")

    elif guess_letter in word:
        for i,w in enumerate(word):
            if w == guess_letter:
                guessd_word[i] = w
        # guess_count -=1
    else:
        print("Incorrect")
        guess_count -=1

    guessed_letters.append(guess_letter)
    print(''.join(guessd_word))
    print()
    return

word = getRandomWord()
guessed_letters = []
guessd_word = list('_' * len(word))
guess_count = 6
print("=" * 5," Welcome to Hangman! ","=" * 5)
print("Word to guess is : ", word)

while guess_count > 0:

    if '_' in guessd_word:
        guess_letter = input("Guess your letter: ").upper()
        playHangman(guess_letter)
        printHang(guess_count)
        print("%i guesses remaining!" % (guess_count))
    else:
        print("You Won! with %i guesses remaining" % (guess_count))
        break
print("The letter was : ", word)
