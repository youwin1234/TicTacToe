def CreateBoard(size):
    board = []
    counter = 0
    for i in range(0,size):
        row = []
        for j in range(0,size):
            row.append(" ")
            counter +=1
        board.append(row)
    return board

def PrintBoard(board):
    for i in range(0,len(board)):
        print(board[i])
def PlayerInput(board,player):
    print("PLAYER " + str(player))
    isLegalMove  = False
    while not isLegalMove:
        pRow = int(input("Enter the row where you'd like to place your symbol (1-" + str(len(board)) + "): ")) - 1
        pCol = int(input("Enter the column where you'd like to place your symbol (1-" + str(len(board)) + "): ")) - 1
        if pRow >= 0 and pRow < len(board) and pCol >= 0 and pCol < len(board):
            if board[pRow][pCol] == " ":
                isLegalMove=True
            else:
                print("That space is already taken! Please choose a valid move.")
        else:
            print("That is outside the range of the board! Please choose a valid move.")
    if player == 1:
        board[pRow][pCol] = "X"
    else:
        board[pRow][pCol] = "O"
def CheckRow(board, row):
    symbol = board[row][0]
    for i in range(0, len(board)):
            if board[row][i] == " " or board[row][i] != symbol:
                return False
    return True
def CheckCol(board, col):
    symbol = board[0][col]
    for i in range(0, len(board)):
            if board[i][col] == " " or board[i][col] != symbol:
                return False
    return True
def CheckDiagUL(board):
    symbol = board[0][0]
    for i in range(0, len(board)):
            if board[i][i] == " " or board[i][i] != symbol:
                return False
    return True
def CheckDiagUR(board):
    symbol = board[0][len(board)-1]
    for i in range(0, len(board)):
                if board[i][len(board)-(i+1)] == " " or board[i][len(board)-(i+1)] != symbol:
                    return False
    return True
#Create the board
board = CreateBoard(3)
isGameWon = False
currentPlayer = 1
numMovesRemaining = len(board)**2
while (not isGameWon) and (numMovesRemaining > 0):
    #Display the Board
    PrintBoard(board)
    #Player Input 
    PlayerInput(board, currentPlayer)
    numMovesRemaining -= 1
    if currentPlayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1
        # Check state
        for i in range(0, len(board)):
            isGameWon = isGameWon or CheckRow(board, i)
            isGameWon = isGameWon or CheckCol(board, i)
        #check row
        #check column
        #check diagonal (top left)
        isGameWon = isGameWon or CheckDiagUL(board)
        #check diagonal (top right)
        isGameWon = isGameWon or CheckDiagUR(board)
#Display end-game content
if not isGameWon:
    print("DRAW")
else:
    if currentPlayer == 1:
        print("Player 1 won!!")
    else: 
        print("Player 2 won!!")
