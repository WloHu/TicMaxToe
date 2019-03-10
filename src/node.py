class Node:

    def __init__(self, board, prev_piece, next_piece, resulting_move=None):

        self.board = board
        self.next_piece = next_piece
        self.prev_piece = prev_piece
        self.value = None
        self.resulting_move = resulting_move
        self._children = []
        self._gen_children()


    @property
    def children(self):
        return self._children

    def _gen_children(self):
        if not self.board.possible_moves():
            self._children = None
        else:
            for elem in self.board.possible_moves():
                board = self.board.copy_board()
                board.make_move(self.next_piece, elem)
                self._children.append(
                    Node(board,
                         prev_piece=self.next_piece,
                         next_piece=self.prev_piece,
                         resulting_move=elem)
                )

    def is_terminal(self):
        return True if not self.board.possible_moves() or self.board.is_winning() else False

    def calc_value(self, prev_max, penalty):

        assert self.is_terminal(), "Cannot calculate value for non-terminal node!"

        if self.board.is_winning() and prev_max:
            self.value = 50 - penalty
        elif self.board.is_winning() and not prev_max:
            self.value = -50 + penalty
        else:
            self.value = 0
