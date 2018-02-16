# This time, we’re going to do exactly the opposite.
# You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

import random

guess_count = 0

def guessIt():
    start = 0
    end = 100
    while True:
        guess = int((start + end)/2)
        print("Is it: ", guess, " ?\n")
        op = int(input("Choose: \n 1- too high\n 2- too low\n 3-correct\n"))
        global guess_count
        guess_count += 1
        if op == 1:
            end = guess
        elif op == 2:
            start = guess
        elif op == 3:
            print(" It took me ",guess_count, " guesses")
            return
        else:
            pass
    return

guessIt()
