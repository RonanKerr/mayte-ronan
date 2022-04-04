
class Board:

    def __init__(self, board_size):
        self.board_size = board_size
        self.game_board = self.create_board()

    def create_board(self):
        board_keys = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                board_keys.append((i, j))
        board = {}
        for i in board_keys:
            board[i] = ' '
        return board

    def change_board(self, coords, game_piece):
        if coords in self.game_board.keys():
            self.game_board[coords] = game_piece
        else:
            raise KeyError

