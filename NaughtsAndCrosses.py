# HarryTurner
# All of this could be done better but Im not that good of a programmer :/

# This are multiple subprocesses or smth that might be able to be used
# for a game of naughts and crosses

#for player1_placement in board: # If there's a space run the command
#                target_index = board.index(player1_placement)
#                board[target_index] = 'x'
#        print_board(board)


# Ideas for any future subprocesses or things - add a '/' when done
# Print the board /
# Add things to the board
# ^ Check to see if any 3 spaces are in a row - put in a seperate subprocess and call in the program after every input
# Add Players /
# Check if boards full /

import re # Used for the check for space

def print_board(board): # Prints out the rows one by one - probs could be more efficient
    print(board[0])
    print(board[1])
    print(board[2])


def players():
    player1 = input("Enter a name for player 1: ")
    # ^ This player is ' x '
    player2 = input("Enter a name for player 2: ")
    # ^ This player is ' o ' - The lowercase oh not zero
    print("These names will be used to tell whose turn it is and who wins")
    return player1 and player2
    # Takes the input for the names and then returns them to be used for other parts of the program
    # The final print statement is just for the players to know why they had to put in names


def check_for_no_space(board):
    res = any(' ' in ele for ele in board) # Checks to see if there is any spaces in any spot in the list
    if res == False:
        print("Board Full") # If there is no spaces print the message
        return True # True for no spaces available
    else:
        print("Board not full") # If there is a space print the message
        return False # False for spaces available
    # Change the output for later, the print messages are just to let me know


# At time of working, Im too mentally drained to do anything, Ill update it later
def input_to_the_board(board):
    player1_point = 0
    player2_point = 0
    print("The ordering goes from 0 to 2: 0,1,2")
    # Whatever you do for player 1, do the same for player 2
    while check_for_no_space != True:
        print(
            "Player 1 input a place on the board by the format of [0] - row and [1] - column")
        print("e.g. [1][0]")
        player1_placement = input()
        if check_for_no_space == False: # Runs the check in the subprocess to see if its worth to do the input
            print("Space is available")
        print_board(board)
    print("Board full with no winner, draw")


board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]] # The board, rows are in different lines to make them look nice

print_board(board)
input_to_the_board(board)
#players()
#print_board(board)
#check_for_no_space(board)
