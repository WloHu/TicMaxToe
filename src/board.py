class Board:

    winning_conditions = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    def __init__(self, state=None):
        if state is not None:
            self.state = state
        else:
            self.state = [None] * 9

    def is_winning(self):
        for elem in self.winning_conditions:
            temp_set = {self.state[x] for x in elem}
            if None not in temp_set and len(temp_set) == 1:
                return True
        return False

    def make_move(self, piece, move):
        self.state[move] = piece

    def possible_moves(self):
        return [i for i, elem in enumerate(self.state) if elem is None]

    def copy_board(self):
        return Board(state=self.state[:])

    def __str__(self):
        return '''
    {0} | {1} | {2}
   -----------
    {3} | {4} | {5}
   -----------
    {6} | {7} | {8}'''.format(*[e if e is not None else " " for e in self.state])
