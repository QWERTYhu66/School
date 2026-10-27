size = 8
board = [[' ' for _ in range(size)] for _ in range(size)]

pieces = ('b', 'w')

board[size // 2 - 1][size // 2 - 1] = pieces[1]
board[size // 2][size // 2] = pieces[1]
board[size // 2 - 1][size // 2] = pieces[0]
board[size // 2][size // 2 - 1] = pieces[0]

def thing(board):
    for row in board:
        print('|' + '|'.join(row) + '|')

thing(board)