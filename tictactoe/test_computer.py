import unittest
from computer import Computer
from game_master import GameMaster
from board import Board


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)
        self.game_master = GameMaster(self.board)
        self.computer = Computer('X', self.game_master)
        
    def test_think_next_move_is_in_board(self):
        self.assertEqual(True, self.computer.think_next_move() < (self.board.board_size, self.board.board_size))


if __name__ == '__main__':
    unittest.main()
