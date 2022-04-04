
class Player:

    def __init__(self, game_piece, game_master):
        self.game_piece = game_piece
        self.game_master = game_master
        self.game_master.players.append(self)
        self.game_master.initialise_players()
        self.win_condition = [0, 0]
        for _ in range(self.game_master.board.board_size):
            self.win_condition.append(0)
            self.win_condition.append(0)

    def try_make_move(self, coords):
        self.game_master.move(coords, self)

    def __repr__(self):
        return f'Player {self.game_piece}'
