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

