def board_display(current_board):
    for i in range(0,3):
        print(current_board[i])

def winmessage():
    print("won")

def check_vertical(current_board):                #for x in range(0,3): 
    for i in range(0,3):                          #     tempvar = current_board[x][i] something like this could work but i cba to figure out how to change a variable name mid loop
        var1 = current_board[0][i]
        var2 = current_board[1][i]
        var3 = current_board[2][i]
        if (var1) and (var2) and (var3) == var1:
            winmessage()

def check_horizontal(current_board):
    for i in range(0,3):                         
        var1 = current_board[i][0]
        var2 = current_board[i][1]
        var3 = current_board[i][2]
        if (var1) and (var2) and (var3) == var1:
            winmessage()

def check_diagonal(current_board):
    var1 = current_board[0][0]
    var2 = current_board[1][1]
    var3 = current_board[2][2]
    var4 = current_board[0][2]
    var5 = current_board[2][0]
    if var1 and var2 and var3 == var1:
        winmessage()
    else:
        if var2 and var4 and var5 == var2:
            winmessage()
        else:
            return
 
def check_spaces(current_board):
    return

def check_if_over(current_board):
    check_vertical(current_board)
    check_horizontal(current_board)
    check_diagonal(current_board)
    check_spaces(current_board)


def get_inputs():
    return


board = [["1","2","3"],
         ["4","5","6"],
         ["7","8","9"]]

board_display(board)
check_if_over(board)
