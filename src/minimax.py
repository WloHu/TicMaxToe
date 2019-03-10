from .eval_method import IEvalMethod

class Minimax(IEvalMethod):

    def __init__(self, root):
        self.root = root

    def evaluate(self):
        _, move = self._max_move(self.root, 0)
        return move

    def _max_move(self, node, depth, prev_max=False):
        max_value = -5000

        if node.is_terminal():
            node.calc_value(False, depth)
            return node.value, node.resulting_move

        for elem in node.children:
            temp_value, _ = self._max_move(elem, depth+1, not prev_max)
            temp_value *= -1
            if temp_value > max_value:
                max_value = temp_value
                best_move = elem.resulting_move
        return max_value, best_move
