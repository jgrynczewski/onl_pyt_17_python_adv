# PEŁNE ROZWIĄZANIE

def show(chessboard):
    """Shows the chessboard in the console.
    DOES NOT WORK UNTIL ALL CLASSES: Pawn, Knight, Queen, King, Rook, Bishop ARE CREATED!!!
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
        Knight: chr(9822),
        Queen: chr(9819),
        King: chr(9818),
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
        self.board = [[None for col in range(8)] for row in range(8)]

    def setup(self):
        figures = []
        # rooks
        figures.extend([
            Rook('white', 0, 0),
            Rook('white', 7, 0),
            Rook('black', 0, 7),
            Rook('black', 7, 7)
        ])

        # knights
        figures.extend([
            Knight('white', 1, 0),
            Knight('white', 6, 0),
            Knight('black', 1, 7),
            Knight('black', 6, 7)
        ])

        # bishops
        figures.extend([
            Bishop('white', 2, 0),
            Bishop('white', 5, 0),
            Bishop('black', 2, 7),
            Bishop('black', 5, 7)
        ])

        # queens
        figures.extend([
            Queen('white', 3, 0),
            Queen('black', 3, 7)
        ])

        # kings
        figures.extend([
            King('white', 4, 0),
            King('black', 4, 7)
        ])

        # pawns
        for idx in range(8):
            figures.extend([
                Pawn('white', idx, 1),
                Pawn('black', idx, 6)
            ])

        # filling the board
        for figure in figures:
            self.board[figure.x][figure.y] = figure

    def list_allowed_moves(self, x, y):
        figure = self.board[x][y]
        if not figure or figure.color != self.color:
            return None

        allowed_moves = figure.list_allowed_moves(self)

        # zad 6 - remove fields occupied by allie figure
        not_occupied_allowed_moves = []
        for move in allowed_moves:
            if self.board[move[0]][move[1]] and self.board[move[0]][move[1]].color == self.color:
                pass
            else:
                not_occupied_allowed_moves.append(move)

        return not_occupied_allowed_moves

    def move(self, from_x, from_y, to_x, to_y):
        allowed_moves = self.list_allowed_moves(from_x, from_y)
        if not allowed_moves or (to_x, to_y) not in allowed_moves:
            raise ValueError

        # Zad 6
        # Nie wymaga zmian dla Knight (Knight po prostu zastępuje figurę, na którą wszedł)

        figure = self.board[from_x][from_y]
        figure.move(to_x, to_y)

        bitted_figure = self.board[to_x][to_y]
        self.board[to_x][to_y] = self.board[from_x][from_y]
        self.board[from_x][from_y] = None

        if bitted_figure and isinstance(bitted_figure, King):
            return f"{self.color.upper()} WON"

        self.color = 'white' if self.color == 'black' else 'black'

    # zad 6

class Figure:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def _get_horizontal_and_vertical_moves(self, chessboard):
        chessboard_length = len(chessboard.board)
        allowed_moves = []

        tmp_x = self.x
        while tmp_x < chessboard_length-1:  # Becarfull! off-by one
            tmp_x += 1
            allowed_moves.append(
                (tmp_x, self.y)
            )
            # zad 6
            if chessboard.board[tmp_x][self.y]:
                break

        tmp_x = self.x
        while tmp_x > 0:
            tmp_x -= 1
            allowed_moves.append(
                (tmp_x, self.y)
            )
            # zad 6
            if chessboard.board[tmp_x][self.y]:
                break

        tmp_y = self.y
        while tmp_y < chessboard_length-1:
            tmp_y += 1
            allowed_moves.append(
                (self.x, tmp_y)
            )
            # zad 6
            if chessboard.board[self.x][tmp_y]:
                break

        tmp_y = self.y
        while tmp_y > 0:
            tmp_y -= 1
            allowed_moves.append(
                (self.x, tmp_y)
            )
            # zad 6
            if chessboard.board[self.x][tmp_y]:
                break

        return allowed_moves

    def _get_diagonal_moves(self, chessboard):
        chessboard_length = len(chessboard.board)
        allowed_moves = []

        tmp_x = self.x
        tmp_y = self.y
        while tmp_x+1 < chessboard_length and tmp_y+1 < chessboard_length:
            if not (tmp_x+1 == self.x and tmp_y+1 == self.y):
                tmp_x += 1
                tmp_y += 1
                allowed_moves.append(
                    (tmp_x, tmp_y)
                )
                # zad 6 - nie mozna przeskakiwac
                if chessboard.board[tmp_x][tmp_y]:
                    break

        tmp_x = self.x
        tmp_y = self.y
        while tmp_x-1 >= 0 and tmp_y-1 >= 0:
            if not (tmp_x-1 == self.x and tmp_y-1 == self.y):
                tmp_x -= 1
                tmp_y -= 1
                allowed_moves.append(
                    (tmp_x, tmp_y)
                )
                # zad 6 - nie mozna przeskakiwac
                if chessboard.board[tmp_x][tmp_y]:
                    break

        tmp_x = self.x
        tmp_y = self.y
        while tmp_x+1 < chessboard_length and tmp_y-1 >= 0:
            if not (tmp_x+1 == self.x and tmp_y-1 == self.y):
                tmp_x += 1
                tmp_y -= 1
                allowed_moves.append(
                    (tmp_x, tmp_y)
                )
                # zad 6 - nie mozna przeskakiwac
                if chessboard.board[tmp_x][tmp_y]:
                    break

        tmp_x = self.x
        tmp_y = self.y
        while tmp_x-1 >= 0 and tmp_y+1 < chessboard_length:
            if not (tmp_x - 1 == self.x and tmp_y + 1 == self.y):
                tmp_x -= 1
                tmp_y += 1
                allowed_moves.append(
                    (tmp_x, tmp_y)
                )
                # zad 6 - nie mozna przeskakiwac
                if chessboard.board[tmp_x][tmp_y]:
                    break

        return allowed_moves


class Pawn(Figure):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.is_moved = False

    def list_allowed_moves(self, chessboard):
        allowed_moves = []
        if self.color == 'white' and self.y+1 < len(chessboard.board):
            # if do zad 6 - nie uwzglednione w testach
            if not chessboard.board[self.x][self.y+1]:
                allowed_moves.append(
                    (self.x, self.y+1),
                )
            if self.y == 1:  # or not self.is_moved
                # if do zad 6
                if not chessboard.board[self.x][self.y+2]:
                    allowed_moves.append(
                        (self.x, self.y+2)
                    )

            # zad 6 bicia
            if (
                    self.x+1 < len(chessboard.board)
                    and
                    chessboard.board[self.x+1][self.y+1]
                    and
                    chessboard.board[self.x+1][self.y+1].color != self.color
                ):
                allowed_moves.append(
                    (self.x+1, self.y+1)
                )
            if chessboard.board[self.x-1][self.y+1] and chessboard.board[self.x-1][self.y+1].color != self.color:
                allowed_moves.append(
                    (self.x-1, self.y+1)
                )

        elif self.color == 'black' and self.y-1 >= 0:
            # if do zad 6
            if not chessboard.board[self.x][self.y-1]:
                allowed_moves.append(
                    (self.x, self.y-1),
                )
            if self.y == 6:  # or not self.is_moved
                # if do zad 6
                if not chessboard.board[self.x][self.y - 2]:
                    allowed_moves.append(
                        (self.x, self.y-2)
                    )

            # zad 6 bicia
            if chessboard.board[self.x-1][self.y-1] and chessboard.board[self.x-1][self.y-1].color != self.color:
                allowed_moves.append(
                    (self.x-1, self.y-1)
                )
            if chessboard.board[self.x+1][self.y-1] and chessboard.board[self.x+1][self.y-1].color != self.color:
                allowed_moves.append(
                    (self.x+1, self.y-1)
                )

        return allowed_moves


class Knight(Figure):
    def list_allowed_moves(self, chessboard):
        chessboard_length = len(chessboard.board)
        allowed_moves = []

        # independent of the color
        if self.y+2 < chessboard_length:
            if self.x+1 < chessboard_length:
                allowed_moves.append(
                    (self.x+1, self.y+2),
                )
            if self.x-1 >= 0:
                allowed_moves.append(
                    (self.x-1, self.y+2)
                )
        if self.y-2 >= 0:
            if self.x+1 < chessboard_length:
                allowed_moves.append(
                    (self.x+1, self.y-2)
                )
            if self.x-1 >= 0:
                allowed_moves.append(
                    (self.x-1, self.y-2)
                )
        if self.y+1 < chessboard_length:
            if self.x+2 < chessboard_length:
                allowed_moves.append(
                    (self.x+2, self.y+1)
                )
            if self.x-2 >= 0:
                allowed_moves.append(
                    (self.x-2, self.y+1)
                )
        if self.y-1 >= 0:
            if self.x+2 < chessboard_length:
                allowed_moves.append(
                    (self.x+2, self.y-1)
                )
            if self.x-2 >= 0:
                allowed_moves.append(
                    (self.x-2, self.y-1)
                )

        return allowed_moves


class Rook(Figure):
    def list_allowed_moves(self, chessboard):
        chessboard_length = len(chessboard.board)
        allowed_moves = []

        tmp_x = self.x
        while tmp_x < chessboard_length-1:  # Becarfull! off-by one
            tmp_x += 1
            allowed_moves.append(
                (tmp_x, self.y)
            )
            # zad 6
            if chessboard.board[tmp_x][self.y]:
                break

        tmp_x = self.x
        while tmp_x > 0:
            tmp_x -= 1
            allowed_moves.append(
                (tmp_x, self.y)
            )
            # zad 6
            if chessboard.board[tmp_x][self.y]:
                break

        tmp_y = self.y
        while tmp_y < chessboard_length-1:
            tmp_y += 1
            allowed_moves.append(
                (self.x, tmp_y)
            )
            # zad 6
            if chessboard.board[self.x][tmp_y]:
                break

        tmp_y = self.y
        while tmp_y > 0:
            tmp_y -= 1
            allowed_moves.append(
                (self.x, tmp_y)
            )
            # zad 6
            if chessboard.board[self.x][tmp_y]:
                break

        return allowed_moves


class King(Figure):
    def list_allowed_moves(self, chessboard):
        chessboard_length = len(chessboard.board)
        allowed_moves = []

        if self.x+1 < chessboard_length:  # here we compare x+1 not x
            if self.y+1 < chessboard_length:
                allowed_moves.append(
                    (self.x+1, self.y+1)
                )
            if self.y-1 >= 0:
                allowed_moves.append(
                    (self.x+1, self.y-1)
                )

            allowed_moves.append(
                (self.x+1, self.y)
            )

        if self.x-1 >= 0:
            if self.y+1 < chessboard_length:
                allowed_moves.append(
                    (self.x-1, self.y+1)
                )
            if self.y-1 >= 0:
                allowed_moves.append(
                    (self.x-1, self.y-1)
                )

            allowed_moves.append(
                (self.x-1, self.y)
            )

        if self.y+1 < chessboard_length:
            allowed_moves.append(
                (self.x, self.y+1)
            )
        if self.y-1 >= 0:
            allowed_moves.append(
                (self.x, self.y-1)
            )

        return allowed_moves


class Bishop(Figure):
    def list_allowed_moves(self, chessboard):
        chessboard_length = len(chessboard.board)
        allowed_moves = []

        tmp_x = self.x
        tmp_y = self.y
        while tmp_x+1 < chessboard_length and tmp_y+1 < chessboard_length:
            if not (tmp_x+1 == self.x and tmp_y+1 == self.y):
                tmp_x += 1
                tmp_y += 1
                allowed_moves.append(
                    (tmp_x, tmp_y)
                )
                # zad 6 - nie mozna przeskakiwac
                if chessboard.board[tmp_x][tmp_y]:
                    break

        tmp_x = self.x
        tmp_y = self.y
        while tmp_x-1 >= 0 and tmp_y-1 >= 0:
            if not (tmp_x-1 == self.x and tmp_y-1 == self.y):
                tmp_x -= 1
                tmp_y -= 1
                allowed_moves.append(
                    (tmp_x, tmp_y)
                )
                # zad 6 - nie mozna przeskakiwac
                if chessboard.board[tmp_x][tmp_y]:
                    break

        tmp_x = self.x
        tmp_y = self.y
        while tmp_x+1 < chessboard_length and tmp_y-1 >= 0:
            if not (tmp_x+1 == self.x and tmp_y-1 == self.y):
                tmp_x += 1
                tmp_y -= 1
                allowed_moves.append(
                    (tmp_x, tmp_y)
                )
                # zad 6 - nie mozna przeskakiwac
                if chessboard.board[tmp_x][tmp_y]:
                    break

        tmp_x = self.x
        tmp_y = self.y
        while tmp_x-1 >= 0 and tmp_y+1 < chessboard_length:
            if not (tmp_x - 1 == self.x and tmp_y + 1 == self.y):
                tmp_x -= 1
                tmp_y += 1
                allowed_moves.append(
                    (tmp_x, tmp_y)
                )
                # zad 6 - nie mozna przeskakiwac
                if chessboard.board[tmp_x][tmp_y]:
                    break

        return allowed_moves


class Queen(Figure):
    def list_allowed_moves(self, chessboard):
        allowed_moves = []

        allowed_moves.extend(self._get_horizontal_and_vertical_moves(chessboard))
        allowed_moves.extend(self._get_diagonal_moves(chessboard))

        return allowed_moves

