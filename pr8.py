# # Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
# #
# # Remember the rules:
# #
# # Rock beats scissors
# # Scissors beats paper
# # Paper beats rock


def rpsGame(player1, player2):
    dif = game_dict.get(player1) - game_dict.get(player2)
    print("dif",dif)
    if dif in [-1,2]:
        global score_pl1
        score_pl1 += 1
        print("Player1 Wins!")
    elif dif in [-2,1]:
        global score_pl2
        score_pl2 += 1
        print("Player2 Wins!")
    else: print("Draw!")
    return

choises = ['rock', 'paper', 'scissor']
game_dict = {'rock':1, 'scissor':2, 'paper':3}
score_pl1 = 0
score_pl2 = 0
while True:
    print('''Please pick one:
            rock
            scissor
            paper''')
    player1 = input("Player 1 -> choose your play: ")
    player2 = input("Player 2 -> choose your play: ")
    rpsGame(player1,player2)
    print("""=====Score Card=====
    Player 1 : {0}
    Player 2 : {1}
    """.format(score_pl1,score_pl2))

    op = input("Start a new game(y/n) :")
    if op.lower() =='n': break
