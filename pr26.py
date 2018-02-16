# If a game of Tic Tac Toe is represented as a list of lists, like so:
#
# game = [
#   [1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]
#   ]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# and a 2 means that player 2 put their token in that space.
# find who win the match using game[]

def col_match(grid):
    for j in range(0,3):
        col = set([grid[0][j], grid[1][j], grid[2][j]])
        print(col)
        if len(col) == 1 and grid[0][j] != 0: #set cannot have duplicate value
            return grid[0][j]
    return 0

def row_match(grid):
    for i in range(0,3):
        row = set([grid[i][0], grid[i][1], grid[i][2]])
        print(row)
        if len(row) == 1 and grid[0][j] != 0: #set cannot have duplicate value
            return grid[0][j]
    return 0
def check_diaonal(grid):
    diag1 = set([grid[1][1],grid[0][2],grid[2][0]])
    print(diag1)

    diag2 = set([grid[1][1],grid[0][0],grid[2][2]])
    print(diag2)

    if len(diag1) == 1 and grid[1][1] != 0:
        return grid[1][1]
    elif len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]
    else:
        return 0

def playTicTac(game_grid):
    if len(game_grid) != 3:
        return
    else:
        diag_result = check_diaonal(game_grid)
        r_result = row_match(game_grid)
        c_result = col_match(game_grid)

        if diag_result:
            print("Player ",diag_result, " Wins!")
        #check if any row matches
        elif r_result:
            print("Player ",r_result, " Wins!")
        #check if any cols matches
        elif c_result:
            print("Player ",c_result, " Wins!")
        else:
            print("Draw!")
    return

game = [
    [1, 2, 2],
	[2, 1, 0],
	[2, 1, 0]
]
winner_is_2 = [
    [2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]
]
winner_is_1 = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]
]

print("Game length: ", len(game))
# grid = []
# grid.append(game[0]).append(game[1]).append(game[2])
# print(grid)

playTicTac(winner_is_2)
