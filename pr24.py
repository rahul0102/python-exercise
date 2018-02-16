# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# Ask the user what size game board they want to draw, and
# draw it for them to the screen using Python’s print statement.

# def drawBoard(rows, cols):
#     pattern = [" ---","|"]
#     for i in range(rows+4):
#         for j in range(cols):
#             if i % 2 == 0:
#                 print(pattern[0], end = " ")
#             else:
#                 print(pattern[1], end = "    ")
#         if i % 2 != 0: print(pattern[1])
#         print("\n")

board_size = input("Enter board size(3 * 3) : ").split("*")
rows = int(board_size[0])
cols = int(board_size[1])
# drawBoard(rows, cols)

for i in range(rows):
    print(" ---" * cols)
    print("|   " * (cols+1),end = "")
    print()
print(" ---" * cols)
