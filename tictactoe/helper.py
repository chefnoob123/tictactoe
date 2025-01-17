def checkRows(board, player):
    
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False
        
def checkColumns(board, player):
    
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkFDiag(board, player):
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    else:
        return False
    
    
def checkSDiag(board, player):
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    else:
        return False
    
    
    