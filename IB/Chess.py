import re

EMPTY = "."
BOARD_SIZE = 8

class Piece:
    white_symbols = {"r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟"}
    symbols = {"r": "♖", "n": "♘", "b": "♗", "q": "♕", "k": "♔", "p": "♙"}

    def __init__(self, white):
        self.white = white

    @property
    def kind(self):
        return self.__class__.__name__[0].lower()

    def __str__(self):
        return (self.white_symbols if self.white else self.symbols)[self.kind]

    def can_move(self, dr, dc, board, r1, c1, r2, c2):
        if self.kind == "p":
            direction = -1 if self.white else 1
            return ((dc == 0 and dr == direction and board[r2][c2] is None) or
                    (abs(dc) == 1 and dr == direction and board[r2][c2] is not None))
        if self.kind == "n":
            return (abs(dr), abs(dc)) in ((1, 2), (2, 1))
        if self.kind == "k":
            return max(abs(dr), abs(dc)) == 1
        valid = ((self.kind == "r" and (dr == 0 or dc == 0)) or
                 (self.kind == "b" and abs(dr) == abs(dc)) or
                 (self.kind == "q" and (dr == 0 or dc == 0 or abs(dr) == abs(dc))))
        if not valid:
            return False
        step_r = 0 if dr == 0 else dr // abs(dr)
        step_c = 0 if dc == 0 else dc // abs(dc)
        return all(board[r1 + i * step_r][c1 + i * step_c] is None
                   for i in range(1, max(abs(dr), abs(dc))))


class Rook(Piece):
    pass


class Knight(Piece):
    @property
    def kind(self):
        return "n"


class Bishop(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass


class Pawn(Piece):
    pass

PIECE_TYPES = {"r": Rook, "n": Knight, "b": Bishop, "q": Queen,
               "k": King, "p": Pawn}


def create_piece(symbol):
    return PIECE_TYPES[symbol.lower()](symbol.isupper())

pieces = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
}
chessboard = (
    [[create_piece(c) for c in "rnbqkbnr"], [create_piece(c) for c in "pppppppp"]]
    + [[None] * BOARD_SIZE for _ in range(4)]
    + [[create_piece(c) for c in "PPPPPPPP"], [create_piece(c) for c in "RNBQKBNR"]]
)
board_flipped = False

def show():
    row_order = range(BOARD_SIZE - 1, -1, -1) if board_flipped else range(BOARD_SIZE)
    col_order = range(BOARD_SIZE - 1, -1, -1) if board_flipped else range(BOARD_SIZE)
    files = "h g f e d c b a" if board_flipped else "a b c d e f g h"
    print("\n  " + files)
    for row in row_order:
        rank = row + 1
        print(rank, " ".join(str(chessboard[row][col]) if chessboard[row][col] else EMPTY
                             for col in col_order), rank)
    print("  " + files)


def is_legal_move(piece, r1, c1, r2, c2, board):
    dr, dc = r2 - r1, c2 - c1
    kind = piece.kind
    if kind == "p":
        direction = -1 if piece.white else 1
        starting_row = 6 if piece.white else 1
        if dc == 0 and dr == direction and board[r2][c2] is None:
            return True
        if (dc == 0 and dr == 2 * direction and r1 == starting_row
                and board[r2][c2] is None and board[r1 + direction][c1] is None):
            return True
        if abs(dc) == 1 and dr == direction and board[r2][c2] is not None:
            return True
        return False
    if kind == "n":
        return (abs(dr), abs(dc)) in ((1, 2), (2, 1))
    if kind == "k":
        return max(abs(dr), abs(dc)) == 1
    if kind == "r" and dr != 0 and dc != 0:
        return False
    if kind == "b" and abs(dr) != abs(dc):
        return False
    if kind == "q" and dr != 0 and dc != 0 and abs(dr) != abs(dc):
        return False
    step_r = 0 if dr == 0 else dr // abs(dr)
    step_c = 0 if dc == 0 else dc // abs(dc)
    return all(board[r1 + i * step_r][c1 + i * step_c] is None
               for i in range(1, max(abs(dr), abs(dc))))


def move(text, white):
    global board_flipped
    notation = text.replace("+", "").replace("#", "")
    # Pawn capture: origin_file x dest_file dest_rank  e.g. "axb5"
    pawn_capture = re.fullmatch(r"([a-h])x([a-h])([1-8])", notation, re.I)
    # Piece capture: [piece?]x dest_file dest_rank  e.g. "Bxc6", "Qxd5", "xc6" (pawn)
    piece_capture = re.fullmatch(r"([KQRBN])?x([a-h])([1-8])", notation, re.I)
    # Non-capture: [piece?]dest_file dest_rank  e.g. "e4", "Nf3", "Bb5"
    match = re.fullmatch(r"([KQRBN])?([a-h])([1-8])", notation, re.I)

    if piece_capture:
        piece_kind = piece_capture.group(1).lower()
        origin_file = None
        destination_file, destination_rank = piece_capture.group(2), piece_capture.group(3)
    elif pawn_capture:
        piece_kind = "p"
        origin_file = pawn_capture.group(1)
        destination_file, destination_rank = pawn_capture.group(2), pawn_capture.group(3)
    elif match:
        piece_kind = (match.group(1) or "P").lower()
        destination_file, destination_rank = match.group(2), match.group(3)
        origin_file = destination_file if piece_kind == "p" else None
    else:
        return False

    r2, c2 = 8 - int(destination_rank), ord(destination_file.lower()) - ord("a")
    if not (0 <= r2 < BOARD_SIZE and 0 <= c2 < BOARD_SIZE):
        return False

    candidates = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = chessboard[row][col]
            if (piece is not None and piece.kind == piece_kind
                    and piece.white == white
                    and (origin_file is None or col == ord(origin_file) - ord("a"))
                    and is_legal_move(piece, row, col, r2, c2, chessboard)):
                candidates.append((row, col))
    if len(candidates) != 1:
        return False
    r1, c1 = candidates[0]

    piece = chessboard[r1][c1]
    destination = chessboard[r2][c2]
    if destination is not None and destination.white == white:
        return False
    chessboard[r2][c2] = piece
    chessboard[r1][c1] = None
    board_flipped = not board_flipped
    return True

def main():
    white = True
    while True:
        show()
        text = input(("White" if white else "Black") + " move (e4, or quit): ")
        if text.lower() == "quit":
            break
        if move(text, white):
            white = not white
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()