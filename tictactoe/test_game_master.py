import unittest
from player import Player
from game_master import GameMaster
from board import Board


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.board = Board(3)
        self.game_master = GameMaster(self.board)
        self.player1 = Player('X', self.game_master)
        self.player2 = Player('O', self.game_master)

    def test_initialise_players(self):
        self.assertEqual(type(self.game_master.player_1), Player)
        self.assertEqual(type(self.game_master.player_2), Player)

    def test_has_player_1_won(self):
        self.player1.win_condition[0] = 3
        self.assertEqual(True, self.game_master.has_player_1_won())

    def test_has_player_2_won(self):
        self.player2.win_condition[0] = 3
        self.assertEqual(True, self.game_master.has_player_2_won())

    def test_is_stalemate(self):
        self.player1.win_condition = [1,1,1,1,1,1,1,1]
        self.player2.win_condition = [2,2,2,2,2,2,2,2]
        self.assertEqual(True, self.game_master.is_stalemate())

    def test_update_win_conditions(self):
        self.player1.try_make_move((0,0))
        self.assertEqual([1,0,0,1,0,0,0,1], self.player1.win_condition)


if __name__ == '__main__':
    unittest.main()
