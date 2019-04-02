import sys
from .players import AiPlayer, HumanPlayer
from .board import Board

class Game:

    def __init__(self):
        self.board = Board()
        self.player1 = self.create_human_player()
        self.player2 = self.create_ai_player()

    def create_human_player(self):
        while True:
            name = input("Please choose X/O: ")
            if name in ("X", "O", "x", "o"):
                break
            else:
                while True:
                    dec = input("Your input is not correct, really want to play? (y/n) ")
                    if dec == 'y':
                        break
                    elif dec == 'n':
                        sys.exit("Bye!")

        return HumanPlayer(name.upper(), self.board)

    def create_ai_player(self):
        return AiPlayer(self.player1.opponent_piece(), self.board)

    def check_board_state(self, win_flag=True):
        if not self.board.possible_moves() and not self.board.is_winning():
            sys.exit("Draw!")
        elif self.board.is_winning() and win_flag:
            sys.exit("Congrats, you win!")
        elif self.board.is_winning() and not win_flag:
            sys.exit("Sorry you loose..")
        else:
            pass

    def play(self):
        print(self.board)
        while self.board.possible_moves() and not self.board.is_winning():
            pos = input("Please enter position (1-9)")
            self.player1.move(int(pos))
            print(self.board)
            self.check_board_state()
            self.player2.move()
            print(self.board)
            self.check_board_state(win_flag=False)

