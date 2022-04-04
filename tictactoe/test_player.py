import unittest
from player import Player
from game_master import GameMaster
from board import Board
from exceptions import IllegalMoveError, Player1WonError, Player2WonError, StalemateError



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)
        self.game_master = GameMaster(self.board)
        self.player1 = Player('X', self.game_master)
        self.player2 = Player('O', self.game_master)

    def test_try_make_move(self):
        self.player1.try_make_move((0, 0))
        self.assertEqual(self.board.game_board[(0, 0)], 'X')

    def test_try_make_move_out_of_board(self):
        self.assertRaises(IllegalMoveError, self.player1.try_make_move, (10, 0))

    def test_try_make_move_not_valid(self):
        self.assertRaises(IllegalMoveError, self.player1.try_make_move, "this isn't even a tuple")

    def test_try_make_move_duplicate(self):
        self.player1.try_make_move((0,0))
        self.assertRaises(IllegalMoveError, self.player1.try_make_move, (0,0))

    def test_try_make_move_player_1_wins(self):
        self.player1.try_make_move((0, 0))
        self.player1.try_make_move((0, 1))
        self.assertRaises(Player1WonError, self.player1.try_make_move, (0, 2))

    def test_try_make_move_player_2_wins(self):
        self.player2.try_make_move((0, 0))
        self.player2.try_make_move((0, 1))
        self.assertRaises(Player2WonError, self.player2.try_make_move, (0, 2))

    def test_try_make_move_stalemate(self):
        self.player1.try_make_move((1, 0))
        self.player1.try_make_move((0, 1))
        self.player1.try_make_move((0, 2))
        self.player2.try_make_move((0, 0))
        self.player2.try_make_move((1, 1))
        self.player2.try_make_move((2, 0))
        self.player2.try_make_move((1, 2))
        self.player2.try_make_move((2, 1))
        self.assertRaises(StalemateError, self.player1.try_make_move, (2, 2))


if __name__ == '__main__':
    unittest.main()
