from exceptions import StalemateError, Player1WonError, Player2WonError, IllegalMoveError


class GameMaster:

    def __init__(self, board):
        self.board = board
        self.game_is_over = False
        self.players = []
        self.player_1 = None
        self.player_2 = None

    def initialise_players(self):
        try:
            self.player_1 = self.players[0]
            self.player_2 = self.players[1]
        except IndexError:
            pass

    def has_player_1_won(self):
        if self.board.board_size in self.player_1.win_condition:
            return True
        else:
            return False

    def has_player_2_won(self):
        if self.board.board_size in self.player_2.win_condition:
            return True
        else:
            return False

    def is_stalemate(self):
        check = [self.board.board_size for _ in range((2*self.board.board_size)+2)]
        if [a + b for a, b in zip(self.player_1.win_condition, self.player_2.win_condition)] == check:
            return True
        else:
            return False

    def is_game_over(self):
        if self.has_player_1_won():
            return self.player_1
        elif self.has_player_2_won():
            return self.player_2
        elif self.is_stalemate():
            return 'stalemate'
        else:
            return None

    def is_move_legal(self, coords):
        try:
            if self.board.game_board[coords] != ' ' or \
                    coords[0] > self.board.board_size - 1 or coords[0] < 0 or \
                    coords[1] > self.board.board_size - 1 or coords[1] < 0:
                return False
            else:
                return True
        except KeyError:
            return False

    def update_win_condition(self, coords, player):
        player.win_condition[coords[0]] += 1
        player.win_condition[coords[1] + self.board.board_size] += 1
        if coords[0] == coords[1]:
            player.win_condition[-1] += 1
        if coords[0] + coords[1] == self.board.board_size - 1:
            player.win_condition[-2] += 1

    def move(self, coords, player):
        if self.is_move_legal(coords):
            self.board.change_board(coords, player.game_piece)
            self.update_win_condition(coords, player)
        else:
            raise IllegalMoveError

        if self.is_game_over() == 'stalemate':
            raise StalemateError
        elif self.is_game_over() == self.player_1:
            raise Player1WonError
        elif self.is_game_over() == self.player_2:
            raise Player2WonError
