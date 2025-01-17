
# Tic Tac Toe Player

import helper
import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():

# return the starting state of the game

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    # Returns player who has the next turn on a board.

    x_count = 0
    o_count = 0
    for i in range(0,3):
        for  j in range(0,3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
            
    if x_count <= o_count:
        return X
    else:
        return O
            
            
                
def actions(board):

    # Returns set of all possible actions (i, j) available on the board.

    actions = set()
    for i in range(0,3):
        for  j in range(0,3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
                
    return actions
    


def result(board, action):
    
    # Returns the board that results from making move (i, j) on the board.
    new_board = copy.deepcopy(board)
    
    if action not in actions(board):
        raise Exception("Not a valid Action")
    try: 
        if player(board) == X:
            new_board[action[0]][action[1]] = X
        else:
            new_board[action[0]][action[1]] = O
            
        return new_board
        
    except: raise Exception("Not a valid move")
        

def winner(board):
    
    # Returns the winner of the game, if there is one.
    
    if helper.checkRows(board, X) or helper.checkColumns(board, X) or helper.checkFDiag(board, X) or helper.checkSDiag(board, X):
        return X
    if helper.checkRows(board, O) or helper.checkColumns(board, O) or helper.checkFDiag(board, O) or helper.checkSDiag(board, O):
        return O
    else:
        return None
    
    


def terminal(board):

    # Returns True if game is over, False otherwise.
    if winner(board):
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    
    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -(math.inf)
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        
    return v    
    

def minimax(board):

    # Returns the optimal action for the current player on the board.
    
    if terminal(board):
        return None
    
    elif player(board) == X:
        plays = []
        
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
            
        return sorted(plays, key = lambda x: x[0], reverse = True)[0][1]
    
    elif player(board) == O:
        plays = []
        
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
            
        return sorted(plays, key = lambda x: x[0])[0][1]
            