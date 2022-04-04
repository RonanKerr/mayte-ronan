import ast
import time
import random

from board import Board
from game_master import GameMaster
from player import Player
from board_printer import BoardPrinter
from save import Save
from human import Human
from computer import Computer
from exceptions import StalemateError, IllegalMoveError, Player1WonError, Player2WonError
from title_screen import TitleScreen


class GameEngine:

    @staticmethod
    def start_two_humans(board, player1, player2):
        current_player = player1
        other_player = player2
        winner = ''
        while winner == '':
            BoardPrinter(board.game_board).print_board()
            user_input = input(f'Player {current_player.game_piece}: ')
            if user_input == 'save':
                print('saving game...')
                Save().save(current_player.game_piece, current_player.win_condition,
                            other_player.game_piece, other_player.win_condition,
                            board.game_board, board.board_size)
            elif user_input == 'quit':
                break
            else:
                try:
                    coords = user_input.split()
                    coords = (int(coords[1]), int(coords[0]))
                    try:
                        current_player.try_make_move(coords)
                        current_player, other_player = other_player, current_player
                    except IllegalMoveError:
                        print('Illegal move')
                    except StalemateError:
                        BoardPrinter(board.game_board).print_board()
                        print('Ended in Stalemate')
                        winner = 'Stalemate'
                    except Player1WonError:
                        BoardPrinter(board.game_board).print_board()
                        print(f'Player {player1.game_piece} won!')
                        winner = player1.game_piece
                    except Player2WonError:
                        BoardPrinter(board.game_board).print_board()
                        print(f'Player {player2.game_piece} won!')
                        winner = player2.game_piece
                except IndexError:
                    pass
                except ValueError:
                    pass

    def start_two_humans_from_save(self):
        save = open('save.txt', 'r', encoding="utf-8")
        lines = save.readlines()
        loaded_board_size = int(lines[5][0])
        loaded_board = Board(loaded_board_size)
        loaded_board.game_board = ast.literal_eval(lines[4])
        save.close()
        loaded_game_master = GameMaster(loaded_board)
        player1 = Player(lines[0][0], loaded_game_master)
        player1.win_condition = ast.literal_eval((lines[1]))
        player2 = Player(lines[2][0], loaded_game_master)
        player2.win_condition = ast.literal_eval((lines[3]))
        self.start_two_humans(loaded_board, player1, player2)

    @staticmethod
    def start_human_computer(board, player1, player2):
        current_player = player1
        other_player = player2
        winner = ''
        while winner == '':
            BoardPrinter(board.game_board).print_board()
            if type(current_player) == Human:
                user_input = input(f'Player {current_player.game_piece}: ')
                if user_input == 'save':
                    print('saving game...')
                    Save().save(current_player.game_piece, current_player.win_condition,
                                other_player.game_piece, other_player.win_condition,
                                board.game_board, board.board_size)
                elif user_input == 'quit':
                    break
                else:
                    try:
                        coords = user_input.split()
                        coords = (int(coords[1]), int(coords[0]))
                        try:
                            current_player.try_make_move(coords)
                            current_player, other_player = other_player, current_player
                        except IllegalMoveError:
                            print('Illegal move')
                        except StalemateError:
                            BoardPrinter(board.game_board).print_board()
                            print('Ended in Stalemate')
                            winner = 'Stalemate'
                        except Player1WonError:
                            BoardPrinter(board.game_board).print_board()
                            print(f'Player {player1.game_piece} won!')
                            winner = player1.game_piece
                        except Player2WonError:
                            BoardPrinter(board.game_board).print_board()
                            print(f'Player {player2.game_piece} won!')
                            winner = player2.game_piece
                    except IndexError:
                        pass
                    except ValueError:
                        pass
            elif type(current_player) == Computer:
                print('The computer is thinking')
                time.sleep(random.randint(0, 30)/10)
                try:
                    current_player.try_make_move(current_player.think_next_move())
                    current_player, other_player = other_player, current_player
                except StalemateError:
                    BoardPrinter(board.game_board).print_board()
                    print('Ended in Stalemate')
                    winner = 'Stalemate'
                except Player1WonError:
                    BoardPrinter(board.game_board).print_board()
                    print(f'Player {player1.game_piece} won!')
                    winner = player1.game_piece
                except Player2WonError:
                    BoardPrinter(board.game_board).print_board()
                    print(f'Player {player2.game_piece} won!')
                    winner = player2.game_piece
                except IndexError:
                    pass
                except ValueError:
                    pass




    def menu(self):
        TitleScreen().print_title()
        print("enter 'help' for a list of commands")
        while True:
            user_input = input("Enter a command: ")
            if user_input == 'new game':
                user_input = input('Board size?: ')
                bad_board = False
                try:
                    board = Board(int(user_input))
                except ValueError:
                    bad_board = True
                if not bad_board:
                    user_input = input('Versus human or computer?: ')
                    if user_input == 'human':
                        game_master = GameMaster(board)
                        player1 = Human('X', game_master)
                        player2 = Human('O', game_master)
                        self.start_two_humans(board, player1, player2)
                    elif user_input == 'computer':
                        game_master = GameMaster(board)
                        player1 = Human('X', game_master)
                        player2 = Computer('O', game_master)
                        self.start_human_computer(board, player1, player2)
                    else:
                        pass
            elif user_input == 'load game':
                self.start_two_humans_from_save()
            elif user_input == 'quit':
                break
            elif user_input == 'help':
                print("new game, load game, quit")




GameEngine().menu()
