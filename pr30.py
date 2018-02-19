# write a function that picks a random word from a list of words from the SOWPODS dictionary. 

import random

words = []
with open('sowpods.txt','r') as f:
    line = f.readline().strip()
    words.append(line)

    while line:
        line = f.readline().strip()
        words.append(line)

rand_word = random.choice(words).strip()
print(rand_word)
