import math

X = 'X'
O = 'O'
EMPTY = None


def initial_state():
    '''
    returns starting state of the board.
    '''
    return [[EMPTY for i in range(3)] for j in range(3)]


def player(board):
    '''
    returns player who has the next turn on a board.
    '''
    x = 0
    o = 0
    for line in board:
        x += line.count(X)
        o += line.count(O)
    if x <= o:
        return X
    return O


def actions(board):
    '''
    returns set of all possible actions (i, j) available on the board.
    '''
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    '''
    returns the board that results from making move (i, j) on the board.
    '''
    player = player(board)
    i, j = action
    board[i][j] = player
    return board


def winner(board):
    '''
    returns the winner of the game, if there is one.
    '''
    for i in range(3):
        prev = board[i][0]
        for j in range(3):
            if board[i][j] == EMPTY:
                break
            elif board[i][j] != prev:
                break
            if j == 2:
                return board[i][j]
    
    for i in range(3):
        prev = board[0][i]
        for j in range(3):
            if board[j][i] == EMPTY:
                break
            elif board[j][i] != prev:
                break
            if j == 2:
                return board[j][i]
    
    if board[1][1] != EMPTY and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]

    return None

def terminal(board):
    '''
    returns True if game is over, False otherwise.
    '''
    for i in range(3):
        prev = board[i][0]
        for j in range(3):
            if board[i][j] == EMPTY:
                break
            elif board[i][j] != prev:
                break
            if j == 2:
                return True
    
    for i in range(3):
        prev = board[0][i]
        for j in range(3):
            if board[j][i] == EMPTY:
                break
            elif board[j][i] != prev:
                break
            if j == 2:
                return True
    
    if board[1][1] != EMPTY and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        return True

    return False


def utility(board):
    '''
    returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    '''
    winner = winner(board)
    if winner == X:
        return 1
    if winner == O:
        return -1
    return 0


def minimax(board):
    '''
    returns the optimal action for the current player on the board.
    '''
    raise NotImplementedError