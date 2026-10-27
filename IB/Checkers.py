size = 8

board = [[' ' for _ in range(size)] for _ in range(size)]

pieces = {
    'r': 'Red',
    'b': 'Black'
}

def thing(board):
    print('  0 1 2 3 4 5 6 7')
    for i, row in enumerate(board):
        print(i, '|' + '|'.join(row) + '|')

def setup():
    for row in range(3):
        for col in range(size):
            if (row + col) % 2 == 1:
                board[row][col] = 'b'

    for row in range(5, 8):
        for col in range(size):
            if (row + col) % 2 == 1:
                board[row][col] = 'r'

def move_piece(player):
    while True:
        thing(board)

        print(pieces[player])
        print("Enter move like: 5 0 4 1")

        move = input("> ").split()

        if len(move) != 4:
            print("Enter 4 numbers.")
            continue

        r1, c1, r2, c2 = map(int, move)

        if not (0 <= r1 < 8 and 0 <= c1 < 8 and 0 <= r2 < 8 and 0 <= c2 < 8):
            print("That is outside the board.")
            continue

        if board[r1][c1] != player:
            print("That is not your piece.")
            continue

        if board[r2][c2] != ' ':
            print("That space is taken.")
            continue

        if abs(c2 - c1) != 1:
            print("You can only move one space diagonally.")
            continue

        if player == 'r' and r2 != r1 - 1:
            print("Red moves up.")
            continue

        if player == 'b' and r2 != r1 + 1:
            print("Black moves down.")
            continue

        board[r1][c1] = ' '
        board[r2][c2] = player
        break

setup()

player = 'r'

while True:
    move_piece(player)

    if player == 'r':
        player = 'b'
    else:
        player = 'r'