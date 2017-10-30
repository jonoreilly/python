"""
Wolf-0
Simple Battleship
From Codecademy - Heavily annotated
"""
# imports a module to make random numbers
from random import randint

# makes a list called 'Board' and populates it with zeroes in a 5 * 5 grid

board = []
for x in range(0, 5):
  board.append(["O"] * 5)
# board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]


# defines a function to print the game board, joining the zeroes in the list with spaces
# looks like this:
"""
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
"""
def print_board(board):
  for row in board:
    print(" ".join(row))

# prints the board one time initially
print_board(board)

# defines two random numbers, one for teh x location and one for the y
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

# creates two variables populated with the random numbers
ship_row = random_row(board)
ship_col = random_col(board)

# begins a loop that gives the user 4 turns (can be changed to any number by editing the range() )
for turn in range(4):

  # asks the player for a guess
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: ")) - 1
  guess_col = int(input("Guess Col: ")) - 1

  # if the guess is correct, congratulate the user and end the loop
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break

  # if the guess is bigger than the board range, state so
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the ocean.")

    # else if the guess has already been made, state so
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already." )

    # else, print that the user missed the battleship
    else:
      print("You missed my battleship!")

      #sets the zero at the guess location to an 'X'
      board[guess_row][guess_col] = "X"
    print_board(board)

    # if the user has made too many turns, end the game
    if turn == 3:
      print('Game Over')
