from abc import ABCMeta, abstractmethod
from .pieces import Pieces
from .node import Node
from .minimax import Minimax

class IPlayer(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        raise NotImplementedError("Please specify evaluation method.")


class HumanPlayer(IPlayer):

    def __init__(self, piece: str, board):

        self.piece = piece
        self.board = board

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, value):
        if value == 'X':
            self._piece = Pieces.X
        else:
            self._piece = Pieces.O

    def move(self, position):
        self.board.make_move(self._piece, position)


class AiPlayer(IPlayer):

    def __init__(self, piece: Pieces, board):
        self._piece = piece
        self.board = board
        self._opponent_piece = self.opponent_piece()

    def opponent_piece(self):
        return Pieces.X if self._piece == Pieces.O else Pieces.O

    def move(self):
        node = Node(self.board, prev_piece=self._opponent_piece, next_piece=self._piece)
        move = Minimax(node).evaluate()
        self.board.make_move(self._piece, move)

