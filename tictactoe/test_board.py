import unittest
from board import Board


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)

    def test_board_constructor(self):
        self.assertEqual(Board, type(self.board))

    def test_board_dimensions(self):
        self.assertEqual(9, len(self.board.game_board.keys()))

    def test_change_board(self):
        self.board.change_board((0,0), 'X')
        self.assertEqual('X',self.board.game_board[(0,0)])

    def test_change_board_key_error(self):
        self.assertRaises(KeyError, self.board.change_board, (0,5), 'X')


if __name__ == '__main__':
    unittest.main()
