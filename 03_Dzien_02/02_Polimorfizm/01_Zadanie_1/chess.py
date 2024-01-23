def show(chessboard):
    """Shows the chessboard in the console.
    DOES NOT WORK UNTIL ALL CLASES: Pawn, Knight, Queen, King, Rook, Bishop ARE CREATED!!!
    """
    WHITE = {
        Pawn: chr(9817),
        Knight: chr(9816),
        Queen: chr(9813),
        King: chr(9812),
        Rook: chr(9814),
        Bishop: chr(9815),
    }
    BLACK = {
        Pawn: chr(9823),
        Knight: chr(9818),
        Queen: chr(9819),
        King: chr(9812),
        Rook: chr(9820),
        Bishop: chr(9821),
    }
    for y in range(7, -1, -1):
        print(y, end='\t')
        for x in range(8):
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color == 'white':
                    print(WHITE[type(chessboard.board[x][y])], end='\t')
                else:
                    print(BLACK[type(chessboard.board[x][y])], end='\t')
            else:
                print('\t', end='')
        print('\n')
    print('\t', end='')
    for x in range(8):
        print(x, end='\t')
    print()


class Chessboard:
    def __init__(self):
        self.color = "white"
        self.board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]


class Pawn:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def list_allowed_moves(self, chessboard):
        allowed_moves = []

        if self.color == "white" and self.y+1 < len(chessboard.board):
            allowed_moves.append(
                (self.x, self.y+1)
            )

            if self.y == 1:
                allowed_moves.append(
                    (self.x, self.y+2)
                )

        if self.color == "black" and self.y-1 >= 0:
            allowed_moves.append(
                (self.x, self.y-1)
            )

            if self.y == len(chessboard.board)-2:
                allowed_moves.append(
                    (self.x, self.y-2)
                )

        return allowed_moves

    def move(self, x, y):
        self.x = x
        self.y = y
