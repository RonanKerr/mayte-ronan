from player import Player
import random


class Computer(Player):

    def think_next_move(self):
        while True:
            random_x = random.randint(0, self.game_master.board.board_size-1)
            random_y = random.randint(0, self.game_master.board.board_size-1)
            if self.game_master.board.game_board[(random_x, random_y)] == ' ':
                return (random_x, random_y)
