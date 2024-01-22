import unittest

import chess


TEST_PAWNS = False
TEST_KNIGHTS = False
TEST_QUEENS = False
TEST_KINGS = False
TEST_ROOKS = False
TEST_BISHOPS = False
TEST_BOARD_SETUP = False
TEST_BOARD_LISTING_MOVES = False
TEST_BOARD_MOVING = False
TEST_PAWNS_KILLING_THE_ENEMY = False
TEST_ROOKS_KILLING_THE_ENEMY = False
TEST_KNIGHTS_KILLING_THE_ENEMY = False
TEST_BISHOPS_KILLING_THE_ENEMY = False
TEST_KINGS_KILLING_THE_ENEMY = False
TEST_QUEENS_KILLING_THE_ENEMY = False
TEST_PAWNS_NOT_KILLING_ALLIES = False
TEST_ROOKS_NOT_KILLING_ALLIES = False
TEST_KNIGHTS_NOT_KILLING_ALLIES = False
TEST_BISHOPS_NOT_KILLING_ALLIES = False
TEST_KINGS_NOT_KILLING_ALLIES = False
TEST_QUEENS_NOT_KILLING_ALLIES = False
TEST_GAME_END = False


unittest.TestCase.maxDiff = None


class ChessboardTestCase(unittest.TestCase):
    def test_attributes_are_in_instance(self):
        cb = chess.Chessboard()
        self.assertTrue(hasattr(cb, 'color'))
        self.assertTrue(hasattr(cb, 'board'))
        self.assertFalse(hasattr(chess.Chessboard, 'color'))
        self.assertFalse(hasattr(chess.Chessboard, 'board'))

    def test_attributes_have_correct_values(self):
        cb = chess.Chessboard()
        self.assertEqual(cb.color, 'white')
        for i in range(8):
            self.assertEqual(len(cb.board[i]), 8)
        if len(set(id(row) for row in cb.board)) != 8:
            self.fail('Wrong number of DISTINCT rows in the board!')


@unittest.skipIf(not TEST_PAWNS, 'These tests are temporarily disabled')
class PawnTestCase(unittest.TestCase):
    def test_saving_color_and_coords(self):
        p1 = chess.Pawn("white", 3, 1)
        p2 = chess.Pawn("black", 4, 6)
        self.assertEqual(p1.color, "white")
        self.assertEqual(p2.color, "black")
        self.assertEqual(p1.x, 3)
        self.assertEqual(p2.x, 4)
        self.assertEqual(p1.y, 1)
        self.assertEqual(p2.y, 6)

    def test_first_moves(self):
        cb = chess.Chessboard()
        p1 = chess.Pawn("white", 3, 1)
        p2 = chess.Pawn("black", 4, 6)
        self.assertCountEqual(p1.list_allowed_moves(cb), [(3, 2), (3, 3)])
        self.assertCountEqual(p2.list_allowed_moves(cb), [(4, 5), (4, 4)])

    def test_subsequent_moves(self):
        cb = chess.Chessboard()
        p1 = chess.Pawn("white", 3, 1)
        p2 = chess.Pawn("black", 4, 6)
        p1.move(3, 3)
        p2.move(4, 4)
        self.assertCountEqual(p1.list_allowed_moves(cb), [(3, 4)])
        self.assertCountEqual(p2.list_allowed_moves(cb), [(4, 3)])

    def test_no_more_moves(self):
        cb = chess.Chessboard()
        p1 = chess.Pawn("white", 3, 6)
        p2 = chess.Pawn("black", 4, 1)
        p1.move(3, 7)
        p2.move(4, 0)
        self.assertCountEqual(p1.list_allowed_moves(cb), [])
        self.assertCountEqual(p2.list_allowed_moves(cb), [])


@unittest.skipIf(not TEST_KNIGHTS, 'These tests are temporarily disabled')
class KnightTestCase(unittest.TestCase):
    def test_saving_color_and_coords(self):
        k1 = chess.Knight("white", 4, 5)
        k2 = chess.Knight("black", 5, 4)
        self.assertEqual(k1.color, "white")
        self.assertEqual(k2.color, "black")
        self.assertEqual(k1.x, 4)
        self.assertEqual(k2.x, 5)
        self.assertEqual(k1.y, 5)
        self.assertEqual(k2.y, 4)

    def test_list_allowed_moves(self):
        cb = chess.Chessboard()
        k1 = chess.Knight("white", 4, 5)
        k2 = chess.Knight("black", 5, 4)
        self.assertCountEqual(
            k1.list_allowed_moves(cb),
            [(5, 7), (6, 6), (6, 4), (5, 3), (3, 3), (2, 4), (2, 6), (3, 7)]
        )
        self.assertCountEqual(
            k2.list_allowed_moves(cb),
            [(6, 6), (7, 5), (7, 3), (6, 2), (4, 2), (3, 3), (3, 5), (4, 6)]
        )

    def test_list_allowed_moves_near_edges(self):
        cb = chess.Chessboard()
        k1 = chess.Knight("white", 0, 0)
        k2 = chess.Knight("black", 7, 7)
        self.assertCountEqual(k1.list_allowed_moves(cb), [(1, 2), (2, 1)])
        self.assertCountEqual(k2.list_allowed_moves(cb), [(6, 5), (5, 6)])

    def test_moving(self):
        k1 = chess.Knight("white", 4, 5)
        k1.move(6, 4)
        self.assertEqual(k1.x, 6)
        self.assertEqual(k1.y, 4)


@unittest.skipIf(not TEST_QUEENS, 'These tests are temporarily disabled')
class QueenTestCase(unittest.TestCase):
    def test_saving_color_and_coords(self):
        q1 = chess.Queen("white", 3, 0)
        q2 = chess.Queen("black", 3, 7)
        self.assertEqual(q1.color, "white")
        self.assertEqual(q2.color, "black")
        self.assertEqual(q1.x, 3)
        self.assertEqual(q2.x, 3)
        self.assertEqual(q1.y, 0)
        self.assertEqual(q2.y, 7)

    def test_list_allowed_moves(self):
        cb = chess.Chessboard()
        q1 = chess.Queen("white", 3, 6)
        q2 = chess.Queen("black", 5, 4)
        self.assertCountEqual(q1.list_allowed_moves(cb), [
            (0, 6), (1, 6), (2, 6), (4, 6), (5, 6), (6, 6), (7, 6), (3, 0),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 7), (0, 3), (1, 4),
            (2, 5), (4, 7), (2, 7), (4, 5), (5, 4), (6, 3), (7, 2)
        ])
        self.assertCountEqual(q2.list_allowed_moves(cb), [
            (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (6, 4), (7, 4), (5, 0),
            (5, 1), (5, 2), (5, 3), (5, 5), (5, 6), (5, 7), (1, 0), (2, 1),
            (3, 2), (4, 3), (6, 5), (7, 6), (2, 7), (3, 6), (4, 5), (6, 3),
            (7, 2)
        ])

    def test_moving(self):
        k1 = chess.Queen("white", 4, 5)
        k1.move(5, 6)
        self.assertEqual(k1.x, 5)
        self.assertEqual(k1.y, 6)


@unittest.skipIf(not TEST_KINGS, 'These tests are temporarily disabled')
class KingTestCase(unittest.TestCase):
    def test_saving_color_and_coords(self):
        k1 = chess.King("white", 4, 5)
        k2 = chess.King("black", 5, 4)
        self.assertEqual(k1.color, "white")
        self.assertEqual(k2.color, "black")
        self.assertEqual(k1.x, 4)
        self.assertEqual(k2.x, 5)
        self.assertEqual(k1.y, 5)
        self.assertEqual(k2.y, 4)

    def test_list_allowed_moves(self):
        cb = chess.Chessboard()
        k1 = chess.King("white", 4, 5)
        k2 = chess.King("black", 5, 4)
        self.assertCountEqual(
            k1.list_allowed_moves(cb),
            [(5, 5), (3, 5), (4, 6), (4, 4), (5, 6), (3, 4), (5, 4), (3, 6)]
        )
        self.assertCountEqual(
            k2.list_allowed_moves(cb),
            [(6, 4), (4, 4), (5, 5), (5, 3), (6, 5), (4, 3), (6, 3), (4, 5)]
        )

    def test_list_allowed_moves_near_edges(self):
        cb = chess.Chessboard()
        k1 = chess.King("white", 0, 0)
        k2 = chess.King("black", 7, 7)
        self.assertCountEqual(k1.list_allowed_moves(cb), [(1, 0), (0, 1), (1, 1)])
        self.assertCountEqual(k2.list_allowed_moves(cb), [(6, 7), (7, 6), (6, 6)])

    def test_moving(self):
        k1 = chess.King("white", 4, 5)
        k1.move(6, 4)
        self.assertEqual(k1.x, 6)
        self.assertEqual(k1.y, 4)


@unittest.skipIf(not TEST_ROOKS, 'These tests are temporarily disabled')
class RookTestCase(unittest.TestCase):
    def test_saving_color_and_coords(self):
        q1 = chess.Rook("white", 3, 0)
        q2 = chess.Rook("black", 3, 7)
        self.assertEqual(q1.color, "white")
        self.assertEqual(q2.color, "black")
        self.assertEqual(q1.x, 3)
        self.assertEqual(q2.x, 3)
        self.assertEqual(q1.y, 0)
        self.assertEqual(q2.y, 7)

    def test_list_allowed_moves(self):
        self.maxDiff = None
        cb = chess.Chessboard()
        q1 = chess.Rook("white", 3, 6)
        q2 = chess.Rook("black", 5, 4)
        self.assertCountEqual(q1.list_allowed_moves(cb), [
            (0, 6), (1, 6), (2, 6), (4, 6), (5, 6), (6, 6), (7, 6), (3, 0),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 7)
        ])
        self.assertCountEqual(q2.list_allowed_moves(cb), [
            (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (6, 4), (7, 4), (5, 0),
            (5, 1), (5, 2), (5, 3), (5, 5), (5, 6), (5, 7)
        ])

    def test_moving(self):
        k1 = chess.Rook("white", 4, 5)
        k1.move(5, 5)
        self.assertEqual(k1.x, 5)
        self.assertEqual(k1.y, 5)
        k1.move(6, 5)
        self.assertEqual(k1.x, 6)
        self.assertEqual(k1.y, 5)


@unittest.skipIf(not TEST_BISHOPS, 'These tests are temporarily disabled')
class BishopTestCase(unittest.TestCase):
    def test_saving_color_and_coords(self):
        q1 = chess.Bishop("white", 3, 0)
        q2 = chess.Bishop("black", 3, 7)
        self.assertEqual(q1.color, "white")
        self.assertEqual(q2.color, "black")
        self.assertEqual(q1.x, 3)
        self.assertEqual(q2.x, 3)
        self.assertEqual(q1.y, 0)
        self.assertEqual(q2.y, 7)

    def test_list_allowed_moves(self):
        self.maxDiff = None
        cb = chess.Chessboard()
        q1 = chess.Bishop("white", 3, 6)
        q2 = chess.Bishop("black", 5, 4)
        self.assertCountEqual(q1.list_allowed_moves(cb), [
            (0, 3), (1, 4), (2, 5), (4, 7), (2, 7), (4, 5), (5, 4), (6, 3), (7, 2)
        ])
        self.assertCountEqual(q2.list_allowed_moves(cb), [
            (1, 0), (2, 1), (3, 2), (4, 3), (6, 5), (7, 6), (2, 7), (3, 6), (4, 5), (6, 3), (7, 2)
        ])

    def test_moving(self):
        k1 = chess.Bishop("white", 4, 5)
        k1.move(5, 6)
        self.assertEqual(k1.x, 5)
        self.assertEqual(k1.y, 6)


@unittest.skipIf(not TEST_BOARD_SETUP, 'These tests are temporarily disabled')
class BoardSetupTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()
        self.cb.setup()

    def test_figures_have_correct_colors_and_coords(self):
        try:
            for x in range(8):
                for y in range(2):
                    self.assertEqual(self.cb.board[x][y].color, "white")
                    self.assertEqual(self.cb.board[x][y].x, x)
                    self.assertEqual(self.cb.board[x][y].y, y)
            for x in range(8):
                for y in range(6, 8):
                    self.assertEqual(self.cb.board[x][y].color, "black")
                    self.assertEqual(self.cb.board[x][y].x, x)
                    self.assertEqual(self.cb.board[x][y].y, y)
        except AssertionError as err:
            raise AssertionError(f'At x={x} y={y}: {str(err)}') from err

    def test_figures_have_correct_types(self):
        try:
            for x, t in enumerate(
                    (chess.Rook, chess.Knight, chess.Bishop, chess.Queen,
                     chess.King, chess.Bishop, chess.Knight, chess.Rook)
            ):
                self.assertTrue(isinstance(self.cb.board[x][0], t))
                self.assertTrue(isinstance(self.cb.board[x][7], t))
        except AssertionError as err:
            raise AssertionError(f'At x={x}: {str(err)}') from err

    def test_pawns_are_in_correct_places(self):
        try:
            for x in range(8):
                self.assertTrue(isinstance(self.cb.board[x][1], chess.Pawn))
                self.assertTrue(isinstance(self.cb.board[x][6], chess.Pawn))
        except AssertionError as err:
            raise AssertionError(f'At x={x}: {str(err)}') from err

    def test_empty_fields_are_empty(self):
        try:
            for x in range(8):
                for y in range(2, 6):
                    self.assertIs(self.cb.board[x][y], None)
        except AssertionError as err:
            raise AssertionError(f'At x={x} y={y}: {str(err)}') from err


@unittest.skipIf(not TEST_BOARD_LISTING_MOVES, 'These tests are temporarily disabled')
class BoardListingMovesTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()
        self.cb.setup()

    def test_board_lists_moves_of_white_piece(self):
        self.assertEqual(self.cb.color, "white")
        self.assertCountEqual(self.cb.list_allowed_moves(2, 1), [(2, 2), (2, 3)])

    def test_board_lists_moves_of_black_piece(self):
        self.cb.color = "black"
        self.assertCountEqual(self.cb.list_allowed_moves(2, 6), [(2, 5), (2, 4)])

    def test_board_does_not_list_moves_for_wrong_player(self):
        self.assertEqual(self.cb.color, "white")
        self.assertIsNone(self.cb.list_allowed_moves(2, 6))

        self.cb.color = "black"
        self.assertIsNone(self.cb.list_allowed_moves(2, 1))

    def test_board_does_not_list_moves_for_empty_spot(self):
        self.assertIsNone(self.cb.list_allowed_moves(4, 4))


@unittest.skipIf(not TEST_BOARD_MOVING, 'These tests are temporarily disabled')
class BoardMovingTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()
        self.cb.setup()

    def test_white_moving(self):
        figure_from_0_1 = self.cb.board[0][1]

        move_result = self.cb.move(0, 1, 0, 3)
        self.assertIsNone(move_result)
        self.assertIsNone(self.cb.board[0][1])
        self.assertIs(self.cb.board[0][3], figure_from_0_1)
        self.assertEqual(self.cb.color, "black")
        self.assertEqual(self.cb.board[0][3].x, 0)
        self.assertEqual(self.cb.board[0][3].y, 3)

    def test_black_moving(self):
        move_result = self.cb.move(0, 1, 0, 3)
        self.assertIsNone(move_result)
        self.assertEqual(self.cb.board[0][3].x, 0)
        self.assertEqual(self.cb.board[0][3].y, 3)

        figure_from_0_6 = self.cb.board[0][6]

        move_result = self.cb.move(0, 6, 0, 4)
        self.assertIsNone(move_result)
        self.assertIsNone(self.cb.board[0][6])
        self.assertIs(self.cb.board[0][4], figure_from_0_6)
        self.assertEqual(self.cb.color, "white")
        self.assertEqual(self.cb.board[0][4].x, 0)
        self.assertEqual(self.cb.board[0][4].y, 4)

    def test_raising_ValueError_on_illegal_moves__no_figure(self):
        with self.assertRaises(ValueError):
            self.cb.move(0, 2, 0, 3)

    def test_raising_ValueError_on_illegal_moves__opponents_figure(self):
        with self.assertRaises(ValueError):
            self.cb.move(0, 6, 0, 4)

    def test_raising_ValueError_on_illegal_moves__invalid_destination(self):
        with self.assertRaises(ValueError):
            self.cb.move(0, 2, 0, 5)


@unittest.skipIf(not TEST_PAWNS_KILLING_THE_ENEMY, 'These tests are temporarily disabled')
class PawnsKillingEnemyTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()
        self.cb.setup()

    def test_white_pawns_can_kill_enemy(self):
        self.cb.board[4][2] = chess.Pawn("black", 4, 2)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 1), [(3, 2), (3, 3), (4, 2)])
        self.assertCountEqual(self.cb.list_allowed_moves(5, 1), [(5, 2), (5, 3), (4, 2)])

    def test_black_pawns_can_kill_enemy(self):
        self.cb.color = 'black'
        self.cb.board[4][5] = chess.Pawn("white", 4, 5)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 6), [(3, 5), (3, 4), (4, 5)])
        self.assertCountEqual(self.cb.list_allowed_moves(5, 6), [(5, 5), (5, 4), (4, 5)])


@unittest.skipIf(not TEST_ROOKS_KILLING_THE_ENEMY, 'These tests are temporarily disabled')
class RooksKillingEnemyTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_rooks_can_kill_enemy(self):
        self.cb.board[3][4] = chess.Rook("white", 3, 4)
        self.cb.board[1][4] = chess.Pawn("black", 1, 4)
        self.cb.board[5][4] = chess.Pawn("black", 5, 4)
        self.cb.board[3][2] = chess.Pawn("black", 3, 2)
        self.cb.board[3][6] = chess.Pawn("black", 3, 6)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(3, 3), (3, 2), (3, 5), (3, 6), (2, 4), (1, 4), (4, 4), (5, 4)])

    def test_black_rooks_can_kill_enemy(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.Rook("black", 3, 4)
        self.cb.board[1][4] = chess.Pawn("white", 1, 4)
        self.cb.board[5][4] = chess.Pawn("white", 5, 4)
        self.cb.board[3][2] = chess.Pawn("white", 3, 2)
        self.cb.board[3][6] = chess.Pawn("white", 3, 6)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(3, 3), (3, 2), (3, 5), (3, 6), (2, 4), (1, 4), (4, 4), (5, 4)])


@unittest.skipIf(not TEST_KNIGHTS_KILLING_THE_ENEMY, 'These tests are temporarily disabled')
class KnightsKillingEnemyTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_knights_can_kill_enemy(self):
        self.cb.board[3][4] = chess.Knight("white", 3, 4)
        self.cb.board[4][6] = chess.Pawn("black", 4, 6)
        self.cb.board[4][2] = chess.Pawn("black", 4, 2)
        self.cb.board[5][5] = chess.Pawn("black", 5, 5)
        self.cb.board[5][3] = chess.Pawn("black", 5, 3)
        self.cb.board[2][6] = chess.Pawn("black", 2, 6)
        self.cb.board[2][2] = chess.Pawn("black", 2, 2)
        self.cb.board[1][5] = chess.Pawn("black", 1, 5)
        self.cb.board[1][3] = chess.Pawn("black", 1, 3)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 6), (4, 2), (5, 5), (5, 3), (2, 6), (2, 2), (1, 5), (1, 3)])

    def test_black_knights_can_kill_enemy(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.Knight("black", 3, 4)
        self.cb.board[4][6] = chess.Pawn("white", 4, 6)
        self.cb.board[4][2] = chess.Pawn("white", 4, 2)
        self.cb.board[5][5] = chess.Pawn("white", 5, 5)
        self.cb.board[5][3] = chess.Pawn("white", 5, 3)
        self.cb.board[2][6] = chess.Pawn("white", 2, 6)
        self.cb.board[2][2] = chess.Pawn("white", 2, 2)
        self.cb.board[1][5] = chess.Pawn("white", 1, 5)
        self.cb.board[1][3] = chess.Pawn("white", 1, 3)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 6), (4, 2), (5, 5), (5, 3), (2, 6), (2, 2), (1, 5), (1, 3)])


@unittest.skipIf(not TEST_BISHOPS_KILLING_THE_ENEMY, 'These tests are temporarily disabled')
class BishopsKillingEnemyTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_bishops_can_kill_enemy(self):
        self.cb.board[3][4] = chess.Bishop("white", 3, 4)
        self.cb.board[5][6] = chess.Pawn("black", 5, 6)
        self.cb.board[1][6] = chess.Pawn("black", 1, 6)
        self.cb.board[1][2] = chess.Pawn("black", 1, 2)
        self.cb.board[5][2] = chess.Pawn("black", 5, 2)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 5), (5, 6), (2, 5), (1, 6), (2, 3), (1, 2), (4, 3), (5, 2)])

    def test_black_bishops_can_kill_enemy(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.Bishop("black", 3, 4)
        self.cb.board[5][6] = chess.Pawn("white", 5, 6)
        self.cb.board[1][6] = chess.Pawn("white", 1, 6)
        self.cb.board[1][2] = chess.Pawn("white", 1, 2)
        self.cb.board[5][2] = chess.Pawn("white", 5, 2)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 5), (5, 6), (2, 5), (1, 6), (2, 3), (1, 2), (4, 3), (5, 2)])


@unittest.skipIf(not TEST_KINGS_KILLING_THE_ENEMY, 'These tests are temporarily disabled')
class KingsKillingEnemyTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_kings_can_kill_enemy(self):
        self.cb.board[3][4] = chess.King("white", 3, 4)
        self.cb.board[2][5] = chess.Pawn("black", 2, 5)
        self.cb.board[3][5] = chess.Pawn("black", 3, 5)
        self.cb.board[4][5] = chess.Pawn("black", 4, 5)
        self.cb.board[2][4] = chess.Pawn("black", 2, 4)
        self.cb.board[4][4] = chess.Pawn("black", 4, 4)
        self.cb.board[2][3] = chess.Pawn("black", 2, 3)
        self.cb.board[3][3] = chess.Pawn("black", 3, 3)
        self.cb.board[4][3] = chess.Pawn("black", 4, 3)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(2, 5), (3, 5), (4, 5), (2, 4), (4, 4), (2, 3), (3, 3), (4, 3)])

    def test_black_kings_can_kill_enemy(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.King("black", 3, 4)
        self.cb.board[2][5] = chess.Pawn("white", 2, 5)
        self.cb.board[3][5] = chess.Pawn("white", 3, 5)
        self.cb.board[4][5] = chess.Pawn("white", 4, 5)
        self.cb.board[2][4] = chess.Pawn("white", 2, 4)
        self.cb.board[4][4] = chess.Pawn("white", 4, 4)
        self.cb.board[2][3] = chess.Pawn("white", 2, 3)
        self.cb.board[3][3] = chess.Pawn("white", 3, 3)
        self.cb.board[4][3] = chess.Pawn("white", 4, 3)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(2, 5), (3, 5), (4, 5), (2, 4), (4, 4), (2, 3), (3, 3), (4, 3)])


@unittest.skipIf(not TEST_QUEENS_KILLING_THE_ENEMY, 'These tests are temporarily disabled')
class QueensKillingEnemyTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_queens_can_kill_enemy(self):
        self.cb.board[3][4] = chess.Queen("white", 3, 4)
        self.cb.board[5][6] = chess.Pawn("black", 5, 6)
        self.cb.board[1][6] = chess.Pawn("black", 1, 6)
        self.cb.board[1][2] = chess.Pawn("black", 1, 2)
        self.cb.board[5][2] = chess.Pawn("black", 5, 2)
        self.cb.board[3][2] = chess.Pawn("black", 3, 2)
        self.cb.board[3][6] = chess.Pawn("black", 3, 6)
        self.cb.board[1][4] = chess.Pawn("black", 1, 4)
        self.cb.board[5][4] = chess.Pawn("black", 5, 4)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 5), (5, 6), (2, 5), (1, 6), (2, 3), (1, 2), (4, 3), (5, 2), (3, 3), (3, 2), (3, 5), (3, 6), (2, 4), (1, 4), (4, 4), (5, 4)])

    def test_black_queens_can_kill_enemy(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.Queen("black", 3, 4)
        self.cb.board[5][6] = chess.Pawn("white", 5, 6)
        self.cb.board[1][6] = chess.Pawn("white", 1, 6)
        self.cb.board[1][2] = chess.Pawn("white", 1, 2)
        self.cb.board[5][2] = chess.Pawn("white", 5, 2)
        self.cb.board[3][2] = chess.Pawn("white", 3, 2)
        self.cb.board[3][6] = chess.Pawn("white", 3, 6)
        self.cb.board[1][4] = chess.Pawn("white", 1, 4)
        self.cb.board[5][4] = chess.Pawn("white", 5, 4)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 5), (5, 6), (2, 5), (1, 6), (2, 3), (1, 2), (4, 3), (5, 2), (3, 3), (3, 2), (3, 5), (3, 6), (2, 4), (1, 4), (4, 4), (5, 4)])


@unittest.skipIf(not TEST_PAWNS_NOT_KILLING_ALLIES, 'These tests are temporarily disabled')
class PawnsNotKillingAlliesTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()
        self.cb.setup()

    def test_white_pawns_do_not_kill_allies(self):
        self.cb.board[4][2] = chess.Pawn("white", 4, 2)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 1), [(3, 2), (3, 3)])
        self.assertCountEqual(self.cb.list_allowed_moves(5, 1), [(5, 2), (5, 3)])

    def test_black_pawns_do_not_kill_allies(self):
        self.cb.color = 'black'
        self.cb.board[4][5] = chess.Pawn("black", 4, 5)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 6), [(3, 5), (3, 4)])
        self.assertCountEqual(self.cb.list_allowed_moves(5, 6), [(5, 5), (5, 4)])


@unittest.skipIf(not TEST_ROOKS_NOT_KILLING_ALLIES, 'These tests are temporarily disabled')
class RooksNotKillingAlliesTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_rooks_do_not_kill_allies(self):
        self.cb.board[3][4] = chess.Rook("white", 3, 4)
        self.cb.board[1][4] = chess.Pawn("white", 1, 4)
        self.cb.board[5][4] = chess.Pawn("white", 5, 4)
        self.cb.board[3][2] = chess.Pawn("white", 3, 2)
        self.cb.board[3][6] = chess.Pawn("white", 3, 6)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(3, 3), (3, 5), (2, 4), (4, 4)])

    def test_black_rooks_do_not_kill_allies(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.Rook("black", 3, 4)
        self.cb.board[1][4] = chess.Pawn("black", 1, 4)
        self.cb.board[5][4] = chess.Pawn("black", 5, 4)
        self.cb.board[3][2] = chess.Pawn("black", 3, 2)
        self.cb.board[3][6] = chess.Pawn("black", 3, 6)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(3, 3), (3, 5), (2, 4), (4, 4)])


@unittest.skipIf(not TEST_KNIGHTS_NOT_KILLING_ALLIES, 'These tests are temporarily disabled')
class KnightsNotKillingAlliesTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_knights_do_not_kill_allies(self):
        self.cb.board[3][4] = chess.Knight("white", 3, 4)
        self.cb.board[4][6] = chess.Pawn("white", 4, 6)
        self.cb.board[4][2] = chess.Pawn("white", 4, 2)
        self.cb.board[5][5] = chess.Pawn("white", 5, 5)
        self.cb.board[5][3] = chess.Pawn("white", 5, 3)
        self.cb.board[2][6] = chess.Pawn("white", 2, 6)
        self.cb.board[2][2] = chess.Pawn("white", 2, 2)
        self.cb.board[1][5] = chess.Pawn("white", 1, 5)
        self.cb.board[1][3] = chess.Pawn("white", 1, 3)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [])

    def test_black_knights_do_not_kill_allies(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.Knight("black", 3, 4)
        self.cb.board[4][6] = chess.Pawn("black", 4, 6)
        self.cb.board[4][2] = chess.Pawn("black", 4, 2)
        self.cb.board[5][5] = chess.Pawn("black", 5, 5)
        self.cb.board[5][3] = chess.Pawn("black", 5, 3)
        self.cb.board[2][6] = chess.Pawn("black", 2, 6)
        self.cb.board[2][2] = chess.Pawn("black", 2, 2)
        self.cb.board[1][5] = chess.Pawn("black", 1, 5)
        self.cb.board[1][3] = chess.Pawn("black", 1, 3)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [])


@unittest.skipIf(not TEST_BISHOPS_NOT_KILLING_ALLIES, 'These tests are temporarily disabled')
class BishopsNotKillingAlliesTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_bishops_do_not_kill_allies(self):
        self.cb.board[3][4] = chess.Bishop("white", 3, 4)
        self.cb.board[5][6] = chess.Pawn("white", 5, 6)
        self.cb.board[1][6] = chess.Pawn("white", 1, 6)
        self.cb.board[1][2] = chess.Pawn("white", 1, 2)
        self.cb.board[5][2] = chess.Pawn("white", 5, 2)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 5), (2, 5), (2, 3), (4, 3)])

    def test_black_bishops_do_not_kill_allies(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.Bishop("black", 3, 4)
        self.cb.board[5][6] = chess.Pawn("black", 5, 6)
        self.cb.board[1][6] = chess.Pawn("black", 1, 6)
        self.cb.board[1][2] = chess.Pawn("black", 1, 2)
        self.cb.board[5][2] = chess.Pawn("black", 5, 2)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 5), (2, 5), (2, 3), (4, 3)])


@unittest.skipIf(not TEST_KINGS_NOT_KILLING_ALLIES, 'These tests are temporarily disabled')
class KingsNotKillingAlliesTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_kings_do_not_kill_allies(self):
        self.cb.board[3][4] = chess.King("white", 3, 4)
        self.cb.board[2][5] = chess.Pawn("white", 2, 5)
        self.cb.board[3][5] = chess.Pawn("white", 3, 5)
        self.cb.board[4][5] = chess.Pawn("white", 4, 5)
        self.cb.board[2][4] = chess.Pawn("white", 2, 4)
        self.cb.board[4][4] = chess.Pawn("white", 4, 4)
        self.cb.board[2][3] = chess.Pawn("white", 2, 3)
        self.cb.board[3][3] = chess.Pawn("white", 3, 3)
        self.cb.board[4][3] = chess.Pawn("white", 4, 3)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [])

    def test_black_kings_do_not_kill_allies(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.King("black", 3, 4)
        self.cb.board[2][5] = chess.Pawn("black", 2, 5)
        self.cb.board[3][5] = chess.Pawn("black", 3, 5)
        self.cb.board[4][5] = chess.Pawn("black", 4, 5)
        self.cb.board[2][4] = chess.Pawn("black", 2, 4)
        self.cb.board[4][4] = chess.Pawn("black", 4, 4)
        self.cb.board[2][3] = chess.Pawn("black", 2, 3)
        self.cb.board[3][3] = chess.Pawn("black", 3, 3)
        self.cb.board[4][3] = chess.Pawn("black", 4, 3)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [])


@unittest.skipIf(not TEST_QUEENS_NOT_KILLING_ALLIES, 'These tests are temporarily disabled')
class QueensNotKillingAlliesTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_queens_do_not_kill_allies(self):
        self.cb.board[3][4] = chess.Queen("white", 3, 4)
        self.cb.board[5][6] = chess.Pawn("white", 5, 6)
        self.cb.board[1][6] = chess.Pawn("white", 1, 6)
        self.cb.board[1][2] = chess.Pawn("white", 1, 2)
        self.cb.board[5][2] = chess.Pawn("white", 5, 2)
        self.cb.board[3][2] = chess.Pawn("white", 3, 2)
        self.cb.board[3][6] = chess.Pawn("white", 3, 6)
        self.cb.board[1][4] = chess.Pawn("white", 1, 4)
        self.cb.board[5][4] = chess.Pawn("white", 5, 4)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 5), (2, 5), (2, 3), (4, 3), (3, 3), (3, 5), (2, 4), (4, 4)])

    def test_black_queens_do_not_kill_allies(self):
        self.cb.color = 'black'
        self.cb.board[3][4] = chess.Queen("black", 3, 4)
        self.cb.board[5][6] = chess.Pawn("black", 5, 6)
        self.cb.board[1][6] = chess.Pawn("black", 1, 6)
        self.cb.board[1][2] = chess.Pawn("black", 1, 2)
        self.cb.board[5][2] = chess.Pawn("black", 5, 2)
        self.cb.board[3][2] = chess.Pawn("black", 3, 2)
        self.cb.board[3][6] = chess.Pawn("black", 3, 6)
        self.cb.board[1][4] = chess.Pawn("black", 1, 4)
        self.cb.board[5][4] = chess.Pawn("black", 5, 4)
        self.assertCountEqual(self.cb.list_allowed_moves(3, 4), [(4, 5), (2, 5), (2, 3), (4, 3), (3, 3), (3, 5), (2, 4), (4, 4)])


@unittest.skipIf(not TEST_GAME_END, 'These tests are temporarily disabled')
class GameEndTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = chess.Chessboard()

    def test_white_win_when_black_king_is_killed(self):
        self.cb.board[4][2] = chess.King("black", 4, 2)
        self.cb.board[3][1] = chess.Pawn("white", 3, 1)
        self.assertEqual(self.cb.move(3, 1, 4, 2), "WHITE WON")

    def test_black_win_when_white_king_is_killed(self):
        self.cb.color = 'black'
        self.cb.board[4][5] = chess.King("white", 4, 5)
        self.cb.board[3][6] = chess.Pawn("black", 3, 6)
        self.assertEqual(self.cb.move(3, 6, 4, 5), "BLACK WON")
