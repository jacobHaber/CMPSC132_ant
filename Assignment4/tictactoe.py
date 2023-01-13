#Jacob Haber

#Variables
playerMoves = [' X ', ' O ']
win = False

board = [[' _ ',' _ ',' _ '],[' _ ',' _ ',' _ '],[' _ ',' _ ',' _ ']]

#displays board
def displayBoard(list):
    #NATE: don't use list as a variable name, it already has a meaning
    for column in range(len(list)):
        for row in range(len(list)):
            print(list[column][row],end="")
        print()


#checks who wins game
# def winCheck(list,turn):
def winCheck(board,turn):
#NATE: pass in the board as a parameter and check that specific board
    #i'm sorry in advanced I haven't done this yet but I already know this is gonna look awful
    # global win
    #Checks for player wins in top row
    if board[0][0] == ' X ' and board[0][1] == ' X ' and board[0][2] == ' X ':
        print("Player 1 wins")
        win = True
    elif board[0][0] == ' O ' and board[0][1] == ' O ' and board[0][2] == ' O ':
        print("Player 2 Wins")
        win = True

    #Checks if player wins middle row
    elif board[1][0] == ' X ' and board[1][1] == ' X ' and board[1][2] == ' X ':
        print("Player 1 wins")
        win = True
    elif board[1][0] == ' O ' and board[1][1] == ' O ' and board[1][2] == ' O ':
        print("Player 2 wins")
        win = True

    #Checks for player win in bottom row
    elif board[2][0] == ' O ' and board[1][1] == ' O ' and board[1][2] == ' O ':
        print("Player 2 wins")
        win = True
    elif board[2][0] == ' X ' and board[1][1] == ' X ' and board[1][2] == ' X ':
        print("Player 2 wins")
        win = True          

    #Checks for player win \ (that way diagonal)
    elif board[0][0] == ' X ' and board[1][1] == ' X ' and board[2][2] == ' X ':
        print("Player 1 wins")
        win = True
    elif board[0][0] == ' O ' and board[1][1] == ' O ' and board[2][2] == ' O ':
        print("Player 2 wins")
        win = True 
   
    #Checks for player win /(otherway way diagonal)
    elif board[0][2] == ' X ' and board[1][1] == ' X ' and board[2][0] == ' X ':
        print("Player 1 wins")
        win = True
    elif board[0][2] == ' O ' and board[1][1] == ' O ' and board[2][0] == ' O ':
        print("Player 2 wins")
        win = True 

    #Checks for player win by column
    elif board[0][0] == ' X ' and board[1][0] == ' X ' and board[2][0] == ' X ':  
            print("Player 1 wins")
            win = True
    elif board[0][0] == ' O ' and board[1][0] == ' O ' and board[2][0] == ' O ':  
            print("Player 2 wins")
            win = True
    elif board[0][1] == ' X ' and board[1][1] == ' X ' and board[2][1] == ' X ':  
            print("Player 1 wins")
            win = True
    elif board[0][1] == ' O ' and board[1][1] == ' O ' and board[2][1] == ' O ':  
            print("Player 2 wins")
            win = True                
    elif board[0][0] == ' X ' and board[1][0] == ' X ' and board[2][0] == ' X ':  
            print("Player 1 wins")
            win = True
    elif board[0][2] == ' O ' and board[1][2] == ' O ' and board[2][2] == ' O ':  
            print("Player 2 wins")
            win = True

    #case where player 1 is bad at the game like really tho player 1 always wins or game is still continuing
    else:
        if turn < 9:
            win = False
        else:
            print("Player 1 and Player 2 tied")
            win = False  
    #I was right :)        
    #NATE: Return win, don't use a global
    return win

def nateCheck(board):
    #NATE: simpler check, takes a board and returns if X or O wins
    pos = [0,1,2]
    #row check
    for i in pos:
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' _ ':
            return board[i][0]
    #col check
    for j in pos:
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != ' _ ':
            return board[0][j]
    #diag check
    for j in pos:
        if board[j][j] == board[j][j] == board[j][j] and board[j][j] != ' _ ':
            return board[j][j]
    for j in pos:
        if board[j][2-j] == board[j][2-j] == board[j][2-j] and board[j][2-j] != ' _ ':
            return board[j][2-j]
       
       
#is the actual game
def actualGame(board, win):
    #determins who gets to place a symbol
    turn = 0
   
    while win == False:
        displayBoard(board)
        #player1 turn
        if turn % 2 == 0:
            playerInputRow = int(input("P1 Enter the row you want to place in(0,1,2): "))
            #moron checker 1.0 row out of bounds
            while playerInputRow > 2 or playerInputRow < 0 :
                playerInputRow = int(input(" Pick a row 0-2 not greater than 2 or less than 0: "))

            playerInputColumn = int(input("P1 Enter the column you want to place in (0,1,2): "))
           
            #moron checker 2.0 column out of bounds
            while playerInputColumn > 2 or playerInputColumn < 0 :
                playerInputColumn = int(input(" Pick a column 0-2 not greater than 2 or less than 0: "))

            #moron checker 3.0 spot taken
            while board[playerInputRow][playerInputColumn] == ' X ' or board[playerInputRow][playerInputColumn] == ' O ':
                displayBoard(board)
                playerInputRow = int(input("P1 Spot was taken Enter a new row you want to place in(0,1,2): "))
                playerInputColumn = int(input("P1 Spot was taken Enter a new column you want to place in (0,1,2): "))
           
            board[playerInputRow][playerInputColumn] = playerMoves[0]
            turn += 1
            winCheck(board,turn)

        #displaysboard so other player has a chance to not be stupid
        displayBoard(board)

        #player 2 turn
        if turn % 2 == 1:    
            playerInputRow = int(input("P2 Enter the row you want to place in(0,1,2): "))
           
            #moron checker 1.0 row is out of bounds
            while playerInputRow > 2 or playerInputRow < 0 :
                playerInputRow = int(input(" Pick a row 0-2 not greater than 2 or less than 0: "))
           
            playerInputRow = int(input("P2 Enter the column you want to place in (0,1,2): "))
           
            #moron checker 2.0 column is out of bounds
            while playerInputColumn > 2 or playerInputColumn < 0 :
                playerInputColumn = int(input(" Pick a column 0-2 not greater than 2 or less than 0: "))
           
            #moron checker 3.0 spot was taken
            while board[playerInputRow][playerInputColumn] == ' X ' or board[playerInputRow][playerInputColumn] == ' O ':
                displayBoard(board)
                playerInputRow = int(input("P2 Spot was taken Enter a new row you want to place in(0,1,2): "))
                playerInputColumn = int(input("P2 Spot was taken Enter a new column you want to place in (0,1,2): "))
           
            #places player 2's O
            board[playerInputRow][playerInputColumn] = playerMoves[1]
           
            turn += 1
            winCheck(board,turn)    
#Game is called
actualGame(board,win)  