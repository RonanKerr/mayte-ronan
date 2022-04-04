
class BoardPrinter:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        index = []
        for key in self.board.keys():
            index.append(key[0])
        board_size = max(index)+1
        padding = len(str(board_size+1))
        board_as_string = ' '
        for i in range(board_size):
            board_as_string = board_as_string + '  ' + str(i) + ' '
        board_as_string = board_as_string + '\n'

        for i in range(board_size):
            board_inter_row = ' '*padding + ' '
            for j in range(board_size):
                board_inter_row += '---+'
            board_inter_row = board_inter_row[0:-1] + '\n'
            board_row = str(i) + '  '
            for j in range(board_size):
                board_row += self.board[(i, j)] + ' | '
            board_row = board_row[0:-2] + '\n'
            board_as_string += board_row + board_inter_row
        board_as_string = board_as_string[0:-len(board_inter_row)-1]
        print(board_as_string)
