from .node import Node

class Minimax:

    def __init__(self, root):
        self.root = root

    def minimax(self):
        _ , move = self.max_move(self.root, 0)
        return move

    def max_move(self, node, depth):
        max_value = -5000
        node.gen_children()

        if node.is_terminal():
            node.calc_value(False, depth)
            return node.value, node.resulting_move

        for elem in node.children:
            temp_value, _ = self.min_move(elem, depth+1)
            if temp_value > max_value:
                max_value = temp_value
                best_move = elem.resulting_move
        return max_value, best_move

    def min_move(self, node, depth):
        min_value = 5000
        node.gen_children()

        if node.is_terminal():
            node.calc_value(True, depth)
            return node.value, node.resulting_move

        for elem in node.children:
            temp_value, _ = self.max_move(elem, depth+1)
            if temp_value < min_value:
                min_value = temp_value
                worst_move = elem.resulting_move
        return min_value, worst_move
