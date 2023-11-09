def board_display(current_board):
    for i in range(0,3):
        print(current_board[i])

def players():  #HARRY BIT
    player1 = input("Enter a name for player 1: ")
    # ^ This player is ' x '
    player2 = input("Enter a name for player 2: ")
    # ^ This player is ' o ' - The lowercase oh not zero
    print("These names will be used to tell whose turn it is and who wins")
    return player1 and player2
    # Takes the input for the names and then returns them to be used for other parts of the program
    # The final print statement is just for the players to know why they had to put in names    #HARRY BIT

def winmessage(winner):
    if winner == "X" or winner == "O":
        print("congratulations ",winner, " You won!")
    else:
        tempvar = "Congratulations the game ended in a draw"


def check_vertical(current_board):                
    for i in range(0,3):                          
        var1 = current_board[0][i]
        var2 = current_board[1][i]
        var3 = current_board[2][i]
        if (var1) == "O" and (var2) == "O" and (var3) == "O" or (var1) == "X" and (var2) == "X" and (var3) == "X":
            if var1 == "X":
                winmessage("X")
            else:
                winmessage("O") 
        else:
            return

def check_horizontal(current_board):
    for i in range(0,3):                         
        var1 = current_board[i][0]
        var2 = current_board[i][1]
        var3 = current_board[i][2]
        if (var1) == "O" and (var2) == "O" and (var3) == "O" or (var1) == "X" and (var2) == "X" and (var3) == "X":
            if var1 == "X":
                winmessage("X")
            else:
                winmessage("O") 
        else:
            return

def check_diagonal(current_board):
    var1 = current_board[0][0]
    var2 = current_board[1][1]
    var3 = current_board[2][2]
    var4 = current_board[0][2]
    var5 = current_board[2][0]
    if (var1) == "X"and (var2) == "X" and (var3) == "X"  or (var1) == "O" and (var2) == "O" and (var3) == "O":
        if var1 == "X":
            winmessage("X")
        else:
            winmessage("O")
    else:
        if (var2) == "X" and (var4) == "X" and (var5) == "X" or (var2) == "O" and (var4) == "O" and (var5) == "O":
            if var2 == "X":
                winmessage("X")
            else:
               winmessage("O") 
        else:
            return


def check_for_no_space(board):  #HARRY BIT
    res = any(' ' in ele for ele in board) # Checks to see if there is any spaces in any spot in the list
    if res == False:
        print("Board Full")
        winmessage("rah")
        return  # True for no spaces available
    else:
        print("") # If there is a space print the message
        return False # False for spaces available
    # Change the output for later, the print messages are just to let me know   HARRY BIT


def check_if_over(current_board): # calls all the other subroutines that check the "state" of the game
    check_vertical(current_board)
    check_horizontal(current_board)
    check_diagonal(current_board)
    check_for_no_space(current_board)

def check_if_spot_is_empty(currentboard,x,y):
    if currentboard[y-1][x-1] != " ":
        print("space occupied no cheating dave")
        print("please pick a valid position")
        return True
    else:
        return
        
    

# At time of working, Im too mentally drained to do anything, Ill update it later  
def input_to_the_board(board,counter):
    if counter % 2 == 1:
        print("Player X's Turn")
    else:
        print("Player O's Turn") 
    playerx = int(input("enter horizontal coordinate: "))
    playery = int(input("enter vertical coordinate: "))
    if check_if_spot_is_empty(board,playerx,playery) == True:
        print("punishment: NO MOVE FOR YOU AHAHHAAHAHHA")
        return
    else:
        if counter % 2 == 1:
         board[playery-1][playerx-1] = "X"
        else:
         board[playery-1][playerx-1] = "O"
    
counter = 0     # gonna increment to change whos player "placement" it is
global gamestatus
gamestatus = 0  # if 0 still playable
                #if 1 X has won
                #if 2 O has won
                #if 3 its a draw

board = [["1 1 ","2 1 ","3 1"],
         ["1 2 ","2 2 ","3 2"],
         ["1 3 ","2 3 ","3 3"]]
board_display(board)
print("this is the coordinate map i cba to fix it atp")

board = [[" "," "," "],
         [" "," "," "],
         ["X","X","X"]]

while gamestatus == 0:
    counter = counter + 1
    board_display(board)
    check_if_over(board)
    input_to_the_board(board,counter)