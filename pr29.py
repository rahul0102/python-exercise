# make a two-player Tic Tac Toe game!
# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
import os
def col_match(grid):
    for j in range(0,3):
        col = set([grid[0][j], grid[1][j], grid[2][j]])
        # print(col)
        if len(col) == 1 and grid[0][j] != 0: #set cannot have duplicate value
            return grid[0][j]
    return 0

def row_match(grid):
    for i in range(0,3):
        row = set([grid[i][0], grid[i][1], grid[i][2]])
        # print(row)
        if len(row) == 1 and grid[0][i] != 0: #set cannot have duplicate value
            return grid[0][i]
    return 0
def check_diaonal(grid):
    diag1 = set([grid[1][1],grid[0][2],grid[2][0]])
    # print(diag1)

    diag2 = set([grid[1][1],grid[0][0],grid[2][2]])
    # print(diag2)

    if len(diag1) == 1 and grid[1][1] != 0:
        return grid[1][1]
    elif len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]
    else:
        return 0

def checkWinner(game_grid):
    if len(game_grid) != 3:
        return 0
    else:
        diag_result = check_diaonal(game_grid)
        r_result = row_match(game_grid)
        c_result = col_match(game_grid)

        if diag_result:
            # print("Player ",diag_result, " Wins!")
            return diag_result
        #check if any row matches
        elif r_result:
            # print("Player ",r_result, " Wins!")
            return r_result
        #check if any cols matches
        elif c_result:
            # print("Player ",c_result, " Wins!")
            return c_result
        else:
            return 0
            # print("Draw!")
    return

def displayGameBord(game_grid, rows = 3, cols = 3):
    symbols = { 0:' ', 1:'O', 2:'X' }

    try:
        os.system('clear') #for windows
    except:
        os.system('clear') #for Linux
    for row_num in range(rows):
        new_row = []
        print(" ---" * cols)
        for col_num in range(cols):
            new_row.append(symbols[game_grid[row_num][col_num]])
        print("| " + " | ".join(new_row) + " |")
        print(" ---" * cols)

def displayResult(winner):
    if winner == 1:
        print("Player 1 Wins!")
        global win_count_pl1
        win_count_pl1 += 1
    elif winner == 2:
        print("Player2 Wins!")
        global win_count_pl2
        win_count_pl2 += 1
    else:
        print("Tie!")

def displayScoreCard(win_count_pl1,win_count_pl2):
    print("=" * 5, " ScoreCard ", "=" * 5)
    print("\tPlayer 1 : ", win_count_pl1)
    print("\tPlayer 2 : ",win_count_pl2)
    print("=" * 23)
    return

def playerTurn(grid, row, col, value):
    if grid[row][col] == 0:
        grid[row][col] = value
    else:
        print("Cannot overide value")
    return grid

def switchPlayer(player):
    if player == 1:
        return 2
    else:
        return 1
def startGame():
    return [[0,0,0] for x in range(3)]

def playTicTac():
    game = startGame()
    displayGameBord(game)
    total_turn = 1
    player = 1
    winner = 0

    while total_turn <= 9 and winner == 0:
        print("Player : ", player)
        available = True #if space available on that block
        while available:
            cord = input("Enter coordinates (x,y) format: (start from (1,1)) ").split(',')
            row = int(cord[0]) - 1
            col =  int(cord[1]) - 1
            if game[row][col] == 0: available = False #space exist so we will use it

        # now add value to that gameBoad
        game = playerTurn(game, row, col , player)
        displayGameBord(game)
        player = switchPlayer(player)

        # check winner if turn is greater than 4
        if total_turn > 4:
            winner = checkWinner(game)

        # one turn finished so do turn ++
        total_turn += 1

    displayResult(winner)

win_count_pl1 = 0
win_count_pl2 = 0

while True:
    playTicTac()
    displayScoreCard(win_count_pl1,win_count_pl2)
    op = input("Want to play again (y/n): ")
    if op.lower() == 'n':
        print("See you later! Have a good day")
        break
