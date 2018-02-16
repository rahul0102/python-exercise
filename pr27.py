# The next logical step is to deal with handling user input.
#  When a player (say player 1, who is X) wants to place an X on the screen,
#  they can’t just click on a terminal. So we are going to approximate this clicking simply by
#  asking the user for a coordinate of where they want to place their piece.

initial_game =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
game_grid = initial_game
total_turn = 9
def playerTurn(grid, row, col, value):
    if grid[row][col] == 0:
        grid[row][col] = value
    else:
        print("Cannot overide value")
    return grid
while total_turn > 0:

    coord_pl1 = input("Player1:\nEnter coordinates (x,y) format: ").split(',')
    total_turn -= 1
    if game_grid[int(coord_pl1[0])][int(coord_pl1[1])] != 0:
        total_turn += 1
        continue
    game_grid = playerTurn(game_grid, int(coord_pl1[0]), int(coord_pl1[1]), "x")
    print(game_grid[0],"\n",game_grid[1],"\n",game_grid[2])

    if total_turn > 0:
        coord_pl2 = input("Player2:\nEnter coordinates (x,y) format: ").split(',')
        total_turn -= 1
        if game_grid[int(coord_pl2[0])][int(coord_pl2[1])] != 0:
            break
        game_grid = playerTurn(game_grid, int(coord_pl2[0]), int(coord_pl2[1]), "o")

        print(game_grid[0],"\n",game_grid[1],"\n",game_grid[2])
